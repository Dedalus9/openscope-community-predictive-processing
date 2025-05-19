from pathlib import Path
from pynwb import NWBHDF5IO
import pandas as pd
import numpy as np
from collections import defaultdict
import warnings

class NwbData:
    def __init__(self, data_path: Path):
        self.data_path = data_path
        self.io=None
        self.nwbfile=None

    def __enter__(self):
        self.io=NWBHDF5IO(str(self.data_path),mode='r')
        self.nwbfile=self.io.read()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.io is not None:
            self.io.close()

    def load_meta_data(self) -> pd.DataFrame:
        dff_obj = self.nwbfile.processing['ophys'].data_interfaces['DfOverF']
        keys = list(dff_obj.roi_response_series.keys())
        shapes = [dff_obj.roi_response_series[key].data.shape for key in keys]

        meta_df = pd.DataFrame({'Key': keys, 'Shape': shapes})
        meta_df['Trial'] = meta_df['Key'].str.extract(r'Trial(\d+)', expand=False).astype(int)
        meta_df_sorted = meta_df.sort_values(by='Trial').reset_index(drop=True)
        return meta_df_sorted
    
    def load_sampling_rate_info(self, dFoverF_data) -> pd.DataFrame:
        trial_rates = []

        # Sort trials by number
        sorted_trials = sorted(dFoverF_data.items(), key=lambda x: x[0])
        first_trial_start_time = sorted_trials[0][1]['time'][0]

        for trial_name, trial_data in sorted_trials:
            t = trial_data['time']
            if len(t) < 2:
                print(f"Warning: Note enough data to estimate rate for {trial_name}")
                continue

            dt = np.diff(t)
            mean_rate = 1 / np.mean(dt)
            median_rate = 1 / np.median(dt)
            std_dt = np.std(dt)

            # Total time
            normed_timestamps = t - t[0]
            total_trial_duration = normed_timestamps[-1]
            trial_start_relative_to_first_trial = t[0] - first_trial_start_time
            trial_end_relative_to_first_trial = t[-1] - first_trial_start_time

            trial_rates.append({
                'Trial': trial_name,
                'Duration': round(total_trial_duration, 3),
                'Trial Start (w.r.t. initial trial)': round(trial_start_relative_to_first_trial, 3),
                'Trial End (w.r.t. initial trial)': round(trial_end_relative_to_first_trial, 3),
                'Mean Rate (Hz)': round(mean_rate, 2),
                'Median Rate (Hz)': round(median_rate, 2),
                'Mean Δt (ms)': round(np.mean(dt) * 1000, 3),
                'Median Δt (ms)': round(np.median(dt) * 1000, 3),
                'Δt Std (ms)': round(std_dt * 1000, 4),
                'Num Frames': len(t),
            })

        rate_df = pd.DataFrame(trial_rates).sort_values('Trial').reset_index(drop=True)
        return rate_df
    
    def load_stimulus_data(self) -> pd.DataFrame:
        stim_table = self.nwbfile.intervals['stimulus_presentations']
        stim_df = stim_table.to_dataframe()
        return stim_df
    
    def load_dFoverF_data(self):
        data_dict = defaultdict(dict)
        dff_obj = self.nwbfile.processing['ophys'].data_interfaces['DfOverF']

        trial_start_times = {}
        trial1_time0=None

        # First pass: find Trial1 start time
        for key in dff_obj.roi_response_series.keys():
            if key.startswith('Trial1'):
                ts = dff_obj.roi_response_series[key]
                if ts.timestamps is None:
                    raise ValueError(f"Timestamps missing for {key}")
                trial1_time0 = ts.timestamps[0]
                t0 = ts.timestamps[0]

                trial_id = key.split('_')[0]
                trial_start_times[trial_id] = min(trial_start_times.get(trial_id, t0), t0)

                if trial_id == 'Trial1':
                    trial1_time0 = t0

        if trial1_time0 is None:
            raise ValueError("Could not find Trial1 to anchor timestamps.")
        
        # Check if Trial1 is the earliest
        earliest_time = min(trial_start_times.values())
        if trial1_time0 > earliest_time:
            warnings.warn(
                f"Trial1 does not have the earliest timestamp. "
                f"Trial1 starts at {trial1_time0:.3f}, but earliest trial starts at {earliest_time:.3f}."
            )
        
        # Second pass: load and normalize all trials relative to Trial1 start
        for key in dff_obj.roi_response_series.keys():
            ts = dff_obj.roi_response_series[key]
            x = ts.data[:].T  # (timepoints, rois)

            if ts.timestamps is None:
                raise ValueError(f"Timestamps missing for {key}")
            t = ts.timestamps[:] - trial1_time0

            trial_str = key.split('_')[0] # e.g., 'Trial1'
            trial_id = int(trial_str.replace('Trial','')) # e.g., 1
            dmd_id = 'DMD1' if 'DMD1' in key else 'DMD2'
            data_dict[trial_id][dmd_id] = x
            data_dict[trial_id]['time'] = t
        return data_dict
    
    def get_roi_meta_data(self):
        img_seg = self.nwbfile.processing['ophys'].data_interfaces['ImageSegmentation']
        plane_segmentations = img_seg.plane_segmentations

        # Ensure it behaves like a dictionary
        if not hasattr(plane_segmentations, 'items'):
            raise TypeError("plane_segmentations is not a dict-like object with `.items()`")

        plane_segmentations_meta_data= dict(plane_segmentations.items())

        return plane_segmentations_meta_data

    def get_roi_masks_by_dmd(self, segmentation_key: str = 'DMD1_plane_segmentation'):
        img_seg = self.nwbfile.processing['ophys'].data_interfaces['ImageSegmentation']
        plane_segmentations = dict(img_seg.plane_segmentations.items())

        if len(plane_segmentations) == 0:
            raise ValueError("No plane segmentations found.")

        if segmentation_key not in plane_segmentations:
            raise KeyError(f"Segmentation '{segmentation_key}' not found. Available: {list(plane_segmentations.keys())}")

        return plane_segmentations[segmentation_key]['image_mask'].data[:]

    def add_stimulus_timeseries(self, dFoverF_data, stim_df, features=('orientation', 'contrast', 'x_position', 'y_position', 'delay',
                                                                    'diameter', 'spatial_frequency', 'temporal_frequency')):
        stim_df = stim_df.copy()
        stim_df['trial']=stim_df['trial'].astype(int)

        for trial_id, trial_data in dFoverF_data.items():
            t = trial_data['time']
            stim_ts = {feat: np.full_like(t,np.nan, dtype=float) for feat in features}

            trial_stimuli = stim_df[stim_df['trial'] == trial_id]

            for _,row in trial_stimuli.iterrows():
                # Find time indices within stimulus window
                stim_mask = (t >= row['start_time']) & (t <= row['stop_time'])
                for feat in features:
                    stim_ts[feat][stim_mask] = row[feat]

            dFoverF_data[trial_id]['stim_ts'] = stim_ts # Dict of np.array_split

        return dFoverF_data