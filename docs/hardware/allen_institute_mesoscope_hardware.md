# Allen Institute Mesoscope Hardware

## Overview

The Mesoscope is an advanced two-photon calcium imaging system developed by the Allen Institute for Neural Dynamics. This cutting-edge microscopy technology enables simultaneous multi-plane imaging of neural activity across multiple brain regions and depths, significantly increasing data collection throughput compared to conventional single-plane two-photon microscopes.

## Dual-Beam Technology

The Allen Institute uses a modified Mesoscope system, also referred to as a "Multiscope," which features innovative dual-beam technology. This design allows researchers to:

- Image multiple cortical depths simultaneously
- Record from two different brain areas in a single experiment
- Acquire data at higher throughput than conventional microscopes

## Technical Specifications

The Dual-Beam Mesoscope consists of three key components:

1. **Delay Line**: Splits the original laser beam into two separate beams and delays one beam by half a period of the excitation laser
2. **Secondary Z-Scanner**: Sends the two beams to different focal planes along the Z-axis
3. **Custom Demultiplexing Unit**: Separates fluorescence from the two planes based on the arrival time at the photodetector

### Key Features:

- **Laser Source**: Ti:Sapphire ultrafast laser (Chameleon Ultra II, Coherent)
- **Pulse Compensation**: Custom-built external pulse compensation module based on a single-prism four-path design
- **Control Software**: Customized ScanImage software (VidrioTech) with an in-house developed Workflow Sequencing Engine
- **Data Acquisition**: National Instruments hardware (PXI chassis, PXIe6363 DAQ boards)
- **Imaging Rate**: 11 Hz per plane (compared to 30 Hz for single-plane systems)
- **Field of View**: Full 5mm field of view for targeting, 400-512 μm for recording
- **Temporal Demultiplexing**: Fluorescence from two planes separated using analog demultiplexing circuit with 6.25 ns integration window

## References

For more detailed information about the Allen Institute's Mesoscope technology:

- [Allen Neural Dynamics website](https://www.allenneuraldynamics.org/)

## Additional Resources

- [Visual Behavior 2P Technical Whitepaper (Allen Brain Observatory)](https://portal.brain-map.org/explore/circuits/visual-behavior-2p)

## Related Documents

- **[Hardware Overview](../hardware-overview.md)**: Summary of all recording platforms used in the project
- **[Experimental Plan](../experimental-plan.md)**: How the Mesoscope is used in different experimental paradigms
- **[Detailed Experimental Plan](../detailed-experimental-plan.md)**: Specific information about Mesoscope recording protocols