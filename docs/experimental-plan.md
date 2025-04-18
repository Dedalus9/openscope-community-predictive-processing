# Experimental Plan

This document outlines the detailed experimental plan for investigating neural mechanisms of predictive processing as part of the OpenScope community project.

## Overview

The OpenScope Community Predictive Processing project involves a series of experiments designed to investigate how the brain processes predictions and prediction errors. These experiments span across different species (mice and primates) and utilize various recording techniques to provide a comprehensive understanding of predictive processing mechanisms.

## Key Research Questions

1. Do temporal, motor, and omission mismatch stimuli engage shared or distinct neural mechanisms?
2. How do these mechanisms differ across species (mice vs. primates)?
3. What computational primitives (e.g., stimulus adaptation, dendritic computation, excitatory/inhibitory balance, hierarchical processing) are central to predictive processing?

## Experimental Paradigms

### 1. Temporal Mismatch Paradigm

In this paradigm, subjects are exposed to stimuli with regular timing patterns that occasionally deviate from the expected timing.

- **Stimuli**: Visual gratings presented at regular intervals with occasional timing deviations
- **Parameters**:
    - Baseline (standard) trials: 960 presentations
    - Mismatch (deviant) trials: 8 presentations
    - Ratio: 120:1 (standard:deviant)
    - Inter-stimulus interval: [TBD]

### 2. Motor Mismatch Paradigm

This paradigm tests how neural responses change when motor actions lead to unexpected sensory outcomes.

- **Setup**: Subjects (mice) run on a wheel while visual stimuli are presented
- **Conditions**:
    - Standard: Visual stimulus coupled with motor action
    - Deviant: Unexpected visual stimulus or absence of expected stimulus following motor action
- **Implementation**: The `Sensory_motor_oddball_slap2.bonsai` workflow controls this experiment

### 3. Omission Mismatch Paradigm

This paradigm examines neural responses when an expected stimulus is omitted entirely.

- **Procedure**: Regular presentation of stimuli with occasional omissions
- **Analysis focus**: Neural activity during the time window when the stimulus would have occurred

## Recording Techniques

1. **In-vivo Two-Photon Imaging**:
    - Used for detailed cellular-level recording
    - Captures activity in specific cell types and compartments (e.g., dendrites)
    - Implementation: SLAP2 system for high-speed imaging

2. **Electrophysiological Recordings**:
    - Neuropixels probes for high-density neural recordings
    - Captures spiking activity and local field potentials

## Species and Brain Regions

1. **Mice**:
    - Primary visual cortex (V1)
    - Higher visual areas
    - Targeted virus injections for cell-type specificity
    - Examples: AAV for expression of iGluSnFR4 in V1 or ASAP8 voltage indicators

2. **Primates** (future/collaborative studies):
    - Homologous visual cortical areas
    - Comparative analysis with mouse data

## Data Analysis Approaches

1. **Single Neuron Analysis**:
    - Response properties to expected vs. unexpected stimuli
    - Adaptation and tuning curves
    - Prediction error signals

2. **Population Dynamics**:
    - Correlation structure
    - Dimensionality reduction techniques
    - Decoding accuracy of expected vs. unexpected stimuli

3. **Computational Modeling**:
    - Model comparison and validation
    - Testing specific hypotheses about predictive processing mechanisms

## Data Sharing and Community Engagement

All data collected through this project will be:
- Formatted according to community standards (e.g., NWB format)
- Shared openly without embargo
- Made available through the Allen Institute or DANDI/NWB archives
- Accompanied by documentation of experimental details

## Current Status and Progress

For the current status of experiments, please refer to:
- The [experiment notes](experiments/) for details on completed sessions
- The [project tracking page](project-tracking.md) for overall progress

## References

1. [Neural mechanisms of predictive processing: a collaborative community experiment through the OpenScope program](https://arxiv.org/abs/2504.09614)