#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate NWB file by creating plots directly from the file

This script reads a SLAP2 NWB file and creates validation plots similar to those
created by the original load_slap2.py script, but directly from the NWB file
using pynwb instead of the original SLAP2 code.

Author: GitHub Copilot (based on original SLAP2 code by Jerome Lecoq)
"""

import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors as mcolors
import argparse
from matplotlib.colors import LinearSegmentedColormap

# Import PyNWB modules
from pynwb import NWBHDF5IO
from pynwb.ophys import TwoPhotonSeries, OpticalChannel, ImageSegmentation, Fluorescence, DfOverF, RoiResponseSeries

def load_nwb_file(nwb_path):
    """
    Load an NWB file
    
    Parameters
    ----------
    nwb_path : str
        Path to the NWB file
        
    Returns
    -------
    nwbfile : NWBFile
        The loaded NWB file
    io : NWBHDF5IO
        The I/O object for the NWB file (needed to close the file properly)
    """
    io = NWBHDF5IO(nwb_path, 'r')
    nwbfile = io.read()
    return nwbfile, io


def validate_nwb(nwb_path, output_dir=None):
    """
    Validate an NWB file by creating plots
    
    Parameters
    ----------
    nwb_path : str
        Path to the NWB file
    output_dir : str, optional
        Path to the output directory for plots
        
    Returns
    -------
    output_dir : str
        Path to the output directory where plots were saved
    """
    # Set default output directory if not provided
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(nwb_path), 'validation')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load NWB file
    nwbfile, io = load_nwb_file(nwb_path)
    
    try:
        # 1. Plot metadata and basic information
        plot_metadata(nwbfile, output_dir)
        
        # 2. Plot stimulus information
        plot_stimulus_info(nwbfile, output_dir)
        
        # 3. Plot summary images
        plot_summary_images(nwbfile, output_dir)
        
        # 4. Plot traces with stimulus overlays
        plot_traces_with_stimuli(nwbfile, output_dir)
        
        # 5. Plot segmentation masks
        plot_segmentation_masks(nwbfile, output_dir)
        
        print(f"Validation plots saved to {output_dir}")
    finally:
        # Close the NWB file
        io.close()
    
    return output_dir


def plot_metadata(nwbfile, output_dir):
    """
    Plot metadata from the NWB file
    
    Parameters
    ----------
    nwbfile : NWBFile
        The NWB file
    output_dir : str
        Path to the output directory for plots
    """
    # Create figure for metadata
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    # Collect metadata
    metadata = [
        f"File ID: {nwbfile.identifier}",
        f"Session Description: {nwbfile.session_description}",
        f"Session Start Time: {nwbfile.session_start_time}",
        f"Experimenter(s): {', '.join(nwbfile.experimenter) if isinstance(nwbfile.experimenter, list) else nwbfile.experimenter}",
        f"Lab: {nwbfile.lab}",
        f"Institution: {nwbfile.institution}",
    ]
    
    # Add subject information if available
    if nwbfile.subject is not None:
        metadata.extend([
            f"Subject ID: {nwbfile.subject.subject_id}",
            f"Species: {nwbfile.subject.species}",
        ])
        
        # Add optional subject fields if they exist
        if hasattr(nwbfile.subject, 'age') and nwbfile.subject.age is not None:
            metadata.append(f"Age: {nwbfile.subject.age}")
        if hasattr(nwbfile.subject, 'sex') and nwbfile.subject.sex is not None:
            metadata.append(f"Sex: {nwbfile.subject.sex}")
        if hasattr(nwbfile.subject, 'genotype') and nwbfile.subject.genotype is not None:
            metadata.append(f"Genotype: {nwbfile.subject.genotype}")
    
    # Add notes if available
    if hasattr(nwbfile, 'notes') and nwbfile.notes is not None:
        metadata.append(f"Notes: {nwbfile.notes}")
    
    # Display metadata
    ax.text(0.05, 0.95, '\n'.join(metadata), va='top', fontsize=12, transform=ax.transAxes)
    
    # Save figure
    plt.title("NWB File Metadata")
    plt.savefig(os.path.join(output_dir, 'metadata.png'), dpi=150, bbox_inches='tight')
    plt.close(fig)


def plot_stimulus_info(nwbfile, output_dir):
    """
    Plot stimulus information from the NWB file
    
    Parameters
    ----------
    nwbfile : NWBFile
        The NWB file
    output_dir : str
        Path to the output directory for plots
    """
    # Get stimulus presentations
    try:
        stim_table = nwbfile.intervals['stimulus_presentations']
        stim_df = stim_table.to_dataframe()
        
        # Plot orientations
        if 'orientation' in stim_df.columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(stim_df['start_time'], stim_df['orientation'], 'bo-', markersize=5)
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Orientation (degrees)')
            ax.set_title('Stimulus Orientations')
            ax.grid(True)
            plt.savefig(os.path.join(output_dir, 'stimulus_orientations.png'), dpi=150, bbox_inches='tight')
            plt.close(fig)
        
        # Plot other parameters if available
        param_columns = [col for col in stim_df.columns if col not in 
                        ['start_time', 'stop_time', 'trial', 'id', 'tags']]
        
        if param_columns:
            fig, axs = plt.subplots(len(param_columns), 1, figsize=(10, 3*len(param_columns)), sharex=True)
            if len(param_columns) == 1:
                axs = [axs]  # Ensure axs is a list-like for consistency
                
            for i, param in enumerate(param_columns):
                if param in stim_df.columns and not stim_df[param].isna().all():
                    axs[i].plot(stim_df['start_time'], stim_df[param], 'o-', markersize=5)
                    axs[i].set_ylabel(param)
                    axs[i].grid(True)
            
            axs[-1].set_xlabel('Time (s)')
            plt.suptitle('Stimulus Parameters')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'stimulus_parameters.png'), dpi=150, bbox_inches='tight')
            plt.close(fig)
        
        # Plot stimulus timing
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, (start, stop) in enumerate(zip(stim_df['start_time'], stim_df['stop_time'])):
            ax.axvspan(start, stop, alpha=0.3, color='gray')
            ax.axvline(start, color='r', linestyle='-', linewidth=1, alpha=0.7)
            ax.axvline(stop, color='b', linestyle='-', linewidth=1, alpha=0.7)
        
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Stimulus')
        ax.set_title('Stimulus Timing')
        ax.set_ylim(0, 1)
        ax.set_yticks([])
        ax.grid(True, axis='x')
        plt.savefig(os.path.join(output_dir, 'stimulus_timing.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)
        
    except (KeyError, AttributeError) as e:
        print(f"Warning: Could not plot stimulus information: {e}")


def plot_summary_images(nwbfile, output_dir):
    """
    Plot summary images from the NWB file
    
    Parameters
    ----------
    nwbfile : NWBFile
        The NWB file
    output_dir : str
        Path to the output directory for plots
    """
    # Find all ImageSeries in acquisition
    summary_images = {}
    for name, acq in nwbfile.acquisition.items():
        if 'ImageSeries' in str(type(acq)):
            summary_images[name] = acq
    
    if summary_images:
        # Create figure for summary images
        num_images = len(summary_images)
        fig_cols = min(3, num_images)
        fig_rows = (num_images + fig_cols - 1) // fig_cols  # Ceiling division
        
        fig, axs = plt.subplots(fig_rows, fig_cols, figsize=(5*fig_cols, 4*fig_rows))
        if num_images == 1:
            axs = np.array([axs])  # Make axs indexable for single subplot
        axs = axs.flatten()
        
        for i, (name, img_series) in enumerate(summary_images.items()):
            if i < len(axs):
                # Get the image data (expecting a 3D array with time as first dimension)
                img_data = img_series.data[:][0]  # Take first time point
                
                # Display the image
                axs[i].imshow(img_data, cmap='viridis')
                axs[i].set_title(name)
                axs[i].axis('off')
        
        # Hide unused subplots
        for j in range(i + 1, len(axs)):
            axs[j].axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'summary_images.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)
    else:
        print("Warning: No summary images found in NWB file")


def plot_traces_with_stimuli(nwbfile, output_dir):
    """
    Plot traces with stimulus overlays from the NWB file
    
    Parameters
    ----------
    nwbfile : NWBFile
        The NWB file
    output_dir : str
        Path to the output directory for plots
    """
    # Get stimulus presentations
    try:
        stim_table = nwbfile.intervals['stimulus_presentations']
        stim_df = stim_table.to_dataframe()
        
        # Get ophys module
        ophys = nwbfile.processing.get('ophys')
        if ophys is None:
            print("Warning: No ophys module found in NWB file")
            return
        
        # Create colormap for stimulus parameters
        base_colors = list(mcolors.TABLEAU_COLORS.values())
        
        # Try to get DfOverF data first (preferred), fallback to Fluorescence
        if 'DfOverF' in ophys.data_interfaces:
            data_interface = ophys.data_interfaces['DfOverF']
            trace_type = 'DfOverF'
        elif 'Fluorescence' in ophys.data_interfaces:
            data_interface = ophys.data_interfaces['Fluorescence']
            trace_type = 'Fluorescence'
        else:
            print("Warning: No DfOverF or Fluorescence data found in NWB file")
            return
        
        # Get ROI response series names (should be per trial)
        roi_series_names = list(data_interface.roi_response_series.keys())
        
        # Group series by trial and DMD (assuming naming convention like 'Trial{trial}_DMD{dmd}')
        trials_dmd = {}
        for name in roi_series_names:
            parts = name.split('_')
            trial_part = [p for p in parts if p.startswith('Trial')]
            dmd_part = [p for p in parts if p.startswith('DMD')]
            
            if trial_part and dmd_part:
                trial_num = int(trial_part[0].replace('Trial', ''))
                dmd_num = int(dmd_part[0].replace('DMD', ''))
                
                if trial_num not in trials_dmd:
                    trials_dmd[trial_num] = {}
                
                trials_dmd[trial_num][dmd_num] = name
        
        # Keep track of previous parameter values for visual cues
        previous_values = {}
        param_colors = {}
        
        # Plot traces for each trial
        for trial_num, dmds in sorted(trials_dmd.items()):
            # Create figure for this trial
            fig = plt.figure(figsize=(10, 8))
            
            # For each DMD
            for i, (dmd_num, series_name) in enumerate(sorted(dmds.items())):
                # Get the ROI response series
                roi_series = data_interface.roi_response_series[series_name]
                
                # Create subplot for this DMD
                ax = plt.subplot(len(dmds), 1, i+1)
                
                # Get trace data and timestamps
                trace_data = roi_series.data[:]  # Shape should be (time, ROI)
                timestamps = roi_series.timestamps[:]
                
                # Get trial start and end times
                trial_start = timestamps[0]
                trial_end = timestamps[-1]
                
                # Get stimuli during this trial
                trial_stims = stim_df[(stim_df['start_time'] >= trial_start) & 
                                     (stim_df['start_time'] <= trial_end)]
                
                # Plot heatmap of traces
                sns.heatmap(trace_data.T, ax=ax, cmap='Greens', 
                           vmin=0, vmax=2)  # Same scale as in load_slap2.py
                
                # Get time tick positions and labels
                num_timepoints = trace_data.shape[0]
                num_ticks = 5
                tick_indices = np.linspace(0, num_timepoints - 1, num_ticks, dtype=int)
                tick_labels = [f"{timestamps[i]:.1f}" for i in tick_indices]
                
                # Set axis labels
                if i == len(dmds) - 1:  # Bottom subplot
                    ax.set_xlabel(f"Time (s) - trial_{trial_num}")
                    ax.set_xticks(tick_indices)
                    ax.set_xticklabels(tick_labels)
                else:
                    ax.set_xticklabels([])
                    ax.set_xticks([])
                
                ax.set_ylabel(f"Synapse # - DMD {dmd_num}")
                
                # Draw vertical bars at stimulus times
                for _, stim_row in trial_stims.iterrows():
                    # Calculate position in the plot
                    stim_time = stim_row['start_time']
                    rel_time = stim_time - trial_start
                    
                    # Convert to x-index in the plot
                    x_index = int(rel_time / (trial_end - trial_start) * (num_timepoints - 1))
                    x_index = max(0, min(x_index, num_timepoints - 1))  # Ensure within bounds
                    
                    # Draw vertical line
                    ax.axvline(x=x_index, color='red', linestyle='-', linewidth=0.5)
                    
                    # Only annotate in the top subplot for clarity
                    if i == 0:
                        # Format stimulus parameters
                        y_offset = -1.5
                        x_offset = 0
                        prev_y_position = 1
                        
                        # Get parameters for this stimulus
                        for param in stim_row.index:
                            if param not in ['start_time', 'stop_time', 'id', 'tags', 'trial']:
                                val = stim_row[param]
                                if pd.notnull(val):  # Skip NaN values
                                    # Format value
                                    try:
                                        formatted_val = f"{float(val):.1g}"
                                    except:
                                        formatted_val = str(val)
                                    
                                    # Get color for this parameter
                                    if param not in param_colors:
                                        param_colors[param] = base_colors[len(param_colors) % len(base_colors)]
                                    
                                    # Check if value has changed
                                    has_changed = previous_values.get(param) != val
                                    previous_values[param] = val
                                    
                                    # Set text properties
                                    color = param_colors[param] if not has_changed else 'black'
                                    weight = 'normal' if not has_changed else 'bold'
                                    
                                    # Adjust y position
                                    adjusted_y_position = prev_y_position + y_offset
                                    prev_y_position = adjusted_y_position
                                    
                                    # Add text
                                    ax.text(x_index + x_offset, adjusted_y_position, 
                                           f"{param}={formatted_val}",
                                           rotation=45,
                                           color=color,
                                           fontsize=8,
                                           fontweight=weight,
                                           ha='left',
                                           va='bottom',
                                           clip_on=False)
            
            # Set overall title and layout
            plt.suptitle(f"Trial {trial_num} - {trace_type}")
            plt.tight_layout()
            
            # Save figure
            plt.savefig(os.path.join(output_dir, f'trial_{trial_num}_traces.png'), dpi=150, bbox_inches='tight')
            plt.close(fig)
            
    except (KeyError, AttributeError) as e:
        print(f"Warning: Could not plot traces: {e}")


def plot_segmentation_masks(nwbfile, output_dir):
    """
    Plot segmentation masks from the NWB file
    
    Parameters
    ----------
    nwbfile : NWBFile
        The NWB file
    output_dir : str
        Path to the output directory for plots
    """
    # Get ophys module
    ophys = nwbfile.processing.get('ophys')
    if ophys is None:
        print("Warning: No ophys module found in NWB file")
        return
    
    # Check if ImageSegmentation exists
    if 'ImageSegmentation' not in ophys.data_interfaces:
        print("Warning: No ImageSegmentation found in NWB file")
        return
    
    # Get ImageSegmentation interface
    img_seg = ophys.data_interfaces['ImageSegmentation']
    
    # Create a folder for segmentation masks
    masks_dir = os.path.join(output_dir, 'segmentation_masks')
    os.makedirs(masks_dir, exist_ok=True)
    
    # Process each plane's segmentation
    for plane_name, plane_seg in img_seg.plane_segmentations.items():
        print(f"Processing segmentation for plane: {plane_name}")
        
        # Get ROI IDs and image mask
        roi_ids = plane_seg.id.data[:]
        roi_mask_list = []
        
        # Check which fields are available for the ROIs
        available_fields = []
        if hasattr(plane_seg, 'image_mask') and plane_seg.image_mask is not None:
            available_fields.append('image_mask')
        if hasattr(plane_seg, 'pixel_mask') and plane_seg.pixel_mask is not None:
            available_fields.append('pixel_mask')
        if hasattr(plane_seg, 'voxel_mask') and plane_seg.voxel_mask is not None:
            available_fields.append('voxel_mask')
        
        if not available_fields:
            print(f"Warning: No mask data found for plane {plane_name}")
            continue
        
        # Create a combined mask for all ROIs in this plane
        if 'image_mask' in available_fields:
            # If image_mask is available, we can directly get the mask dimensions
            first_mask = plane_seg.image_mask[0]
            height, width = first_mask.shape
            combined_mask = np.zeros((height, width), dtype=np.int32)
            
            # Collect all masks for individual visualizations
            for i, roi_id in enumerate(roi_ids):
                mask = plane_seg.image_mask[i]
                roi_mask_list.append(mask)
                # Add to combined mask with ROI index as the value
                combined_mask[mask > 0] = i + 1  # +1 to avoid 0 (background)
        
        elif 'pixel_mask' in available_fields:
            # For pixel masks, we need to determine the dimensions first
            # by finding the maximum x and y coordinates
            max_x = 0
            max_y = 0
            
            # First pass: determine dimensions
            for i in range(len(roi_ids)):
                pixel_mask = plane_seg.pixel_mask[i]
                for pixel in pixel_mask:
                    y, x = int(pixel[0]), int(pixel[1])
                    max_y = max(max_y, y)
                    max_x = max(max_x, x)
            
            # Add 1 to get the correct dimensions (0-based indexing)
            height, width = max_y + 1, max_x + 1
            
            # Create empty combined mask
            combined_mask = np.zeros((height, width), dtype=np.int32)
            
            # Second pass: fill in the masks
            for i, roi_id in enumerate(roi_ids):
                pixel_mask = plane_seg.pixel_mask[i]
                individual_mask = np.zeros((height, width), dtype=np.float32)
                
                for pixel in pixel_mask:
                    y, x, value = int(pixel[0]), int(pixel[1]), pixel[2]
                    individual_mask[y, x] = value
                    combined_mask[y, x] = i + 1  # +1 to avoid 0 (background)
                
                roi_mask_list.append(individual_mask)
        
        # Create a colormap for visualization
        colors = plt.cm.viridis(np.linspace(0, 1, len(roi_ids) + 1))
        custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)
        
        # Plot combined masks
        plt.figure(figsize=(10, 10))
        plt.imshow(combined_mask, cmap=custom_cmap)
        plt.colorbar(label='ROI Index')
        plt.title(f'All ROIs - {plane_name} ({len(roi_ids)} ROIs)')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(os.path.join(masks_dir, f'{plane_name}_all_masks.png'), dpi=150, bbox_inches='tight')
        plt.close()
        
        # Plot individual masks - arrange in a grid
        rows_per_figure = 5
        cols_per_figure = 6
        masks_per_figure = rows_per_figure * cols_per_figure
        
        # Calculate number of figures needed
        num_figures = (len(roi_mask_list) + masks_per_figure - 1) // masks_per_figure
        
        for fig_idx in range(num_figures):
            start_idx = fig_idx * masks_per_figure
            end_idx = min(start_idx + masks_per_figure, len(roi_mask_list))
            
            fig, axs = plt.subplots(rows_per_figure, cols_per_figure, 
                                   figsize=(15, 12), 
                                   gridspec_kw={'wspace': 0.1, 'hspace': 0.1})
            axs = axs.flatten()
            
            for i, mask_idx in enumerate(range(start_idx, end_idx)):
                axs[i].imshow(roi_mask_list[mask_idx], cmap='viridis')
                axs[i].set_title(f'ROI {roi_ids[mask_idx]}', fontsize=8)
                axs[i].axis('off')
            
            # Hide unused subplots
            for j in range(end_idx - start_idx, masks_per_figure):
                axs[j].axis('off')
                axs[j].set_visible(False)
            
            plt.suptitle(f'{plane_name} - ROI Masks (Page {fig_idx+1}/{num_figures})', fontsize=14)
            plt.tight_layout()
            plt.savefig(os.path.join(masks_dir, f'{plane_name}_masks_page{fig_idx+1}.png'), dpi=150, bbox_inches='tight')
            plt.close()
        
        # Create a visualization with ROI outlines overlaid on each other
        plt.figure(figsize=(10, 10))
        
        # Create a colored visualization where ROIs are semi-transparent
        overlay = np.zeros((height, width, 4))  # RGBA array
        
        for i, mask in enumerate(roi_mask_list):
            # Get a distinct color for this ROI
            color_idx = i % len(colors)
            r, g, b, a = colors[color_idx]
            
            # Create a mask for this ROI with its color
            roi_rgba = np.zeros((height, width, 4))
            roi_rgba[mask > 0, 0] = r
            roi_rgba[mask > 0, 1] = g
            roi_rgba[mask > 0, 2] = b
            roi_rgba[mask > 0, 3] = 0.3  # Semi-transparent
            
            # Add to overlay
            overlay[roi_rgba[:, :, 3] > 0] = roi_rgba[roi_rgba[:, :, 3] > 0]
            
            # Draw outline
            from scipy import ndimage
            edges = mask - ndimage.binary_erosion(mask)
            y_indices, x_indices = np.where(edges > 0)
            plt.scatter(x_indices, y_indices, s=0.5, color=(r, g, b), alpha=0.8)
        
        plt.imshow(overlay)
        plt.title(f'ROI Outlines - {plane_name} ({len(roi_ids)} ROIs)')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(os.path.join(masks_dir, f'{plane_name}_roi_outlines.png'), dpi=150, bbox_inches='tight')
        plt.close()
        
        # If summary images are available, plot ROI outlines on top of summary images
        summary_images = {}
        for name, acq in nwbfile.acquisition.items():
            if 'ImageSeries' in str(type(acq)):
                summary_images[name] = acq
        
        for img_name, img_series in summary_images.items():
            try:
                # Get the image data (expecting a 3D array with time as first dimension)
                img_data = img_series.data[:][0]  # Take first time point
                
                if img_data.shape[:2] == (height, width):  # Check if dimensions match
                    plt.figure(figsize=(10, 10))
                    plt.imshow(img_data, cmap='gray')
                    
                    # Overlay ROI outlines
                    for i, mask in enumerate(roi_mask_list):
                        # Get a distinct color for this ROI
                        color_idx = i % len(colors)
                        r, g, b, a = colors[color_idx]
                        
                        # Draw outline
                        from scipy import ndimage
                        edges = mask - ndimage.binary_erosion(mask)
                        y_indices, x_indices = np.where(edges > 0)
                        plt.scatter(x_indices, y_indices, s=0.5, color=(r, g, b), alpha=0.8)
                    
                    plt.title(f'ROI Outlines on {img_name} - {plane_name}')
                    plt.axis('off')
                    plt.tight_layout()
                    plt.savefig(os.path.join(masks_dir, f'{plane_name}_roi_on_{img_name}.png'), dpi=150, bbox_inches='tight')
                    plt.close()
            except Exception as e:
                print(f"Warning: Could not overlay ROIs on {img_name}: {e}")
    
    print(f"Segmentation mask plots saved to {masks_dir}")


def main():
    parser = argparse.ArgumentParser(description='Validate NWB file by creating plots')
    parser.add_argument('--nwb', type=str, required=True, 
                        help='Path to NWB file')
    parser.add_argument('--output', type=str, default=None,
                        help='Output directory for plots (default: "validation" folder next to NWB file)')
    
    args = parser.parse_args()
    
    validate_nwb(args.nwb, args.output)


if __name__ == "__main__":
    main()