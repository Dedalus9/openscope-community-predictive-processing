# Sensory-Motor Closed-Loop Stimulus

## Overview

The Sensory-Motor Closed-Loop stimulus provides a visual environment where the movement of the mouse (via a running wheel) directly controls the phase of drifting gratings. This creates a closed sensorimotor loop that allows investigation of how neural responses are modulated by self-generated visual feedback. **Note: While the script is named "Sensory_motor_oddball_slap2.bonsai", the oddball paradigm has not yet been implemented - this is currently only a closed-loop script.**

## Script Location

The stimulus script is located at:
- [`/code/stimulus-control/src/Sensory_motor_oddball_slap2.bonsai`](https://github.com/allenneuraldynamics/openscope-community-predictive-processing/blob/main/code/stimulus-control/src/Sensory_motor_oddball_slap2.bonsai)

## Hardware Requirements

- SLAP2 imaging system
- Behavior device with encoder/wheel for tracking animal movement
- Running wheel connected to an encoder on Port 2

## Stimulus Parameters

### Basic Parameters
- **Display Type**: Drifting gratings
- **Spatial Frequency**: 0.04 cycles per degree
- **Temporal Frequency**: 0 Hz (static, since motion is controlled by the wheel)
- **Contrast**: 1.0 (full contrast)
- **Size**: 90° (covering a large portion of the visual field)
- **Aperture**: 90°
- **Angle**: 0° (horizontal grating)

## Experimental Design

### Closed-Loop Sensorimotor Integration
The core of this experiment is the direct coupling between:

1. **Mouse Movement**: Rotary encoder on Port 2 tracks the animal's wheel running
2. **Visual Feedback**: Encoder data is used to update the phase of the visual gratings in real-time

This creates a predictable relationship where:
- Forward wheel movement → Forward grating motion
- Backward wheel movement → Backward grating motion
- Stationary → Static grating

The script implements this coupling by:
- Reading encoder values from the behavior device
- Dividing encoder values by 300 to create an appropriate scaling factor
- Using the modulus of 360 to convert the wheel position to grating phase
- Applying this calculated phase to the gratings in real-time

### Technical Implementation
- Encoder values are acquired at high frequency and published to a subject called "Encoder"
- The DrawGratings workflow subscribes to this encoder data
- Real-time mapping applies encoder position to grating phase
- The temporal frequency parameter is set to 0 Hz as the movement is controlled by the wheel

## Future Development

This script is designed as a foundation for a future Sensory-Motor Oddball paradigm, where occasional violations of the predictable sensorimotor contingency will be introduced. However, the oddball component has not yet been implemented in this version.

Planned future additions include:
- Introducing mismatches between wheel movement and visual feedback
- Adding different types of sensory-motor contingency violations

## Data Collection

Running data is collected via an encoder on Port 2 of the behavior device.

## Synchronization
- SLAP2 recording is automatically started and stopped during the experiment
- The experiment can be controlled via spacebar (start) and End key (stop)

## Running the Experiment
1. Start the Bonsai workflow
2. Press the spacebar to begin the experiment
3. The mouse can then control the gratings by running on the wheel
4. The experiment can be terminated with the End key

## Expected Neural Responses
This paradigm is designed to elicit neural activity patterns related to:
1. Visuomotor integration
2. Self-generated vs. externally generated sensory feedback
3. Predictive coding in sensorimotor loops

## Related Documents

- **[Bonsai Instructions](bonsai_instructions.md)**: Setup and deployment of Bonsai code
- **[Experimental Plan](../experimental-plan.md)**: Overview of all experimental paradigms
- **[SLAP2 Hardware](../hardware/allen_institute_slap2_hardware.md)**: Details about the SLAP2 imaging system
- **[Standard Oddball](standard-oddball.md)**: Information about the related standard oddball paradigm
