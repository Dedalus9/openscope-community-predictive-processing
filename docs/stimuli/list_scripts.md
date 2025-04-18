# Oddball Session Scripts

This document provides an overview of the scripts specifically used for oddball experimental protocols in this project.

## Oddball Protocol Scripts

1. **Standard_oddball_slap2.bonsai** - Standard oddball protocol optimized for SLAP2 hardware
   - For detailed information, see [Standard Oddball Protocol](standard-oddball.md)
   - Located in `code/stimulus-control/src/`

2. **Sensory_motor_oddball_slap2.bonsai** - Implements the sensory-motor oddball paradigm for SLAP2 hardware
   - For detailed information, see [Sensory-Motor Closed Loop Protocol](sensory-motor-closed-loop.md)
   - Located in `code/stimulus-control/src/`

## Instructions

For instructions on how to set up and run these Bonsai scripts, please refer to:
- [Bonsai Instructions](bonsai_instructions.md)

## How to Add a Script to This Documentation

To add a new script to this documentation:

1. Place your Bonsai script in the appropriate location, typically in `code/stimulus-control/src/`

2. Update this file (`list_scripts.md`) by adding the script name and a brief description in the relevant section

3. If your script implements a new experimental protocol, create a dedicated markdown file in the `docs/stimuli/` directory that explains:
   - The purpose of the protocol
   - Key parameters and settings
   - How to run the script
   - Expected outputs and data formats
   - Any hardware-specific considerations

4. Update the `mkdocs.yml` file at the root of the repository to include your new markdown file in the navigation structure