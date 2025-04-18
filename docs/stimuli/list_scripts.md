# Oddball Session Scripts

This document provides an overview of the scripts specifically used for oddball experimental protocols in this project.

## Standard Oddball Protocol

- **Standard_oddball.bonsai** - The standard oddball protocol script (generic version)
    - Located in `code/stimulus-control/src/`
    - For detailed information, see [Standard Oddball Protocol](standard-oddball.md)

- **Standard_oddball_slap2.bonsai** - Standard oddball protocol optimized for SLAP2 hardware
    - Located in `code/stimulus-control/src/`
    - For detailed information, see [Standard Oddball Protocol](standard-oddball.md)

## Sensory-Motor Oddball Protocol

- **Sensory_motor_oddball_slap2.bonsai** - Implements the sensory-motor oddball paradigm for SLAP2 hardware
    - Located in `code/stimulus-control/src/`
    - For detailed information, see [Sensory-Motor Closed Loop Protocol](sensory-motor-closed-loop.md)

## Bonsai Instructions

For instructions on how to set up and run these Bonsai scripts, please refer to:
- [Bonsai Instructions](bonsai_instructions.md)

## Adding a New Script to Documentation

If you've created a new script that should be added to this documentation, follow these steps:

1. Place your Bonsai script in `code/stimulus-control/src/`

2. Add your script to this list with a brief description

3. For a new experimental protocol, create a markdown file in `docs/stimuli/` explaining:
    - Protocol purpose
    - Key parameters and settings
    - Running instructions
    - Output formats
    - Hardware considerations

4. Update `mkdocs.yml` to include your new markdown file