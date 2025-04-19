# Hardware Documentation

This page provides an overview of the hardware setups used in the OpenScope Community Predictive Processing project. Each hardware configuration has been carefully selected to support specific aspects of the experimental design.

## Overview of Recording Systems

The project utilizes three primary recording systems:

1. **SLAP2 (Swept Line Active Polarization)** - For high-speed subcellular imaging
2. **Neuropixels Probes** - For high-density electrophysiological recordings
3. **Mesoscope** - For wide-field calcium imaging

Each system offers unique advantages for studying predictive processing mechanisms at different spatial and temporal scales.

---

## Quick Links to Detailed Hardware Documentation

- [SLAP2 Setup](hardware/allen_institute_slap2_hardware.md) - High-speed subcellular imaging
- [Neuropixels Setup](hardware/allen_institute_neuropixels_hardware.md) - High-density neural recordings
- [Mesoscope Setup](hardware/allen_institute_mesoscope_hardware.md) - Wide-field calcium imaging

---

## Hardware Selection Rationale

### Two-Photon Imaging (SLAP2)

Two-photon calcium imaging using the SLAP2 system provides:
- Cellular-level recording with the ability to track specific cell types
- Ability to image dendrites and somata simultaneously
- Access to genetically defined cell populations through viral labeling

This approach is ideal for studying:
- Cell-type specific contributions to predictive processing
- Dendritic computation during prediction and surprise
- Layer-specific dynamics in cortical circuits

### Neuropixels Recordings

Neuropixels probes enable:
- Millisecond-precision spike timing across hundreds of neurons
- Simultaneous recording from multiple brain regions
- Layer-specific activity patterns

This approach is crucial for:
- Determining the precise timing of prediction signals
- Tracking prediction-related activity across distributed networks
- Relating spike timing to local field potentials

### Wide-Field Imaging (Mesoscope)

The mesoscope system allows:
- Simultaneous imaging across multiple cortical regions
- Tracking of global activity patterns
- Low-resolution but high-coverage neural recordings

This approach helps with:
- Identifying which brain regions participate in different prediction tasks
- Understanding large-scale dynamics during prediction formation
- Relating local processing to global brain states

---

## Hardware Integration

All hardware systems are integrated with the same stimulus delivery system to ensure comparability of results. The Bonsai software framework is used for stimulus presentation, hardware synchronization, and data logging.

For details on stimulus implementation, see the [Bonsai Instructions](stimuli/bonsai_instructions.md).