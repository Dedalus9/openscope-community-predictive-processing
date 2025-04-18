# Detailed Experimental Plan

This document outlines the comprehensive experimental plan for investigating neural mechanisms of predictive processing as part of the OpenScope community project. This plan is designed to resolve existing divergences between experimental and theoretical domains and deepen our understanding of the mechanisms underlying predictive processing.

## Background and Scientific Context

Recent research reveals that the brain employs various mechanisms for predictive processing, which may vary depending on the nature and difficulty of prediction tasks. Our review of the literature identified key computational primitives that may support predictive processing:

1. **Stimulus adaptation**: Neurons adjust their responses to recurring stimuli, potentially enhancing sensitivity to change
2. **Dendritic computation**: Integration of multiple inputs within a neuron, supporting prediction error calculation
3. **Excitatory/inhibitory (E/I) balance**: Different inhibitory subtypes provide a framework for complex predictions
4. **Hierarchical processing**: Multi-level processing across brain areas enables sophisticated, multi-modal predictions

Evidence suggests that mechanisms of predictive processing differ across paradigms. For example:
- In visual oddball paradigms, prediction errors are mostly limited to layer 2/3 pyramidal neurons
- In auditory sensorimotor paradigms, mismatch responses occur in both layer 5 and layer 2/3
- In somatosensory oddball paradigms, prediction errors have been identified across multiple layers

## Key Research Questions

This project aims to address the following key questions:

1. Do temporal, motor, and omission mismatch stimuli engage shared or distinct neural mechanisms?
2. How do these mechanisms differ across species (mice vs. primates)?
3. What computational primitives are central to predictive processing?

## Alternative Hypotheses

We are testing two alternative hypotheses:

- **H0**: Mechanisms of predictive processing fundamentally differ depending on predictive set and prediction error types, recruiting different neuronal mechanisms.
- **H1**: A unified predictive processing mechanism drives all mismatch processing in the mammalian cortex.

## Experimental Design

### 1. Stimulus Set Design

Our stimulus set includes several validated mismatch stimuli designed to enable the study of:
- Synaptic adaptation
- Positive and negative errors
- Short-term memory through local recurrence
- E/I balance

All experiments will feature sequences of drifting gratings with five types of oddballs:
1. Drifting grating halt
2. Two alternative drifting orientations
3. Omission
4. Temporal jittered oddballs

These oddballs will be introduced in four different session contexts:

#### Session 1 – Standard Mismatch
Animals will be habituated to a series of drifting gratings of the same orientation. Various mismatch stimuli will be introduced randomly: differing orientations, omissions, and spatial oddballs.

#### Session 2 – Sensorimotor Mismatch
Animals will be habituated to a closed-loop visuo-motor running disk where disk rotation directly controls visual flow on a screen. The same mismatch stimuli as in Session 1 will be introduced.

#### Session 3 – Sequence Mismatch
Animals will be habituated to rapid sequences of 4 stimuli. The sequences will repeat once per second for 37 minutes. The same mismatch stimuli as in Session 1 will be introduced in the third position of the sequence, once every 11 seconds on average.

#### Session 4 – Temporal Mismatch
Animals will be exposed to a sequence of drifting gratings with the same orientation. Some gratings will have durations that are either shorter or longer than expected. The session will alternate between fixed blocks (consistent grating durations) and jittered blocks (variable durations).

### 2. Recording Techniques

To evaluate the relative contributions of different mechanisms, we will use two complementary approaches:

1. **Two-photon imaging**:
    - Ideal for recording from different classes of inhibitory neurons in dense networks
    - Provides cellular-level recording with the ability to track specific cell types
    - Will capture activity in specific cell types and compartments (e.g., dendrites)

2. **Neuropixels recordings**:
    - Captures spike timing with high temporal resolution
    - Allows for recording from multiple brain regions simultaneously
    - Provides broad coverage across brain regions and layers

### 3. Species and Brain Regions

1. **Mice**:
    - Primary visual cortex (V1)
    - Higher visual areas (LM)
    - Motor areas (M1, M2)
    - Prefrontal cortex
    - LGN

2. **Primates** (collaborative studies):
    - V1, V2, V3
    - MT/MST
    - Prefrontal cortex

### 4. Recording Sessions

Sessions will be organized across 4 cohorts:
- Two cohorts using two-photon imaging (pan-excitatory and pan-inhibitory GCAMP lines)
- Two cohorts using Neuropixels recordings (with SST-optotagging)

Each mouse will be chronically recorded across either:
- 8 sessions (two-photon imaging) 
- 4 sessions (Neuropixels recording)

Each session will include habituated stimuli, oddball blocks, and control blocks.

## Multi-lab Collaboration

In addition to recordings performed by the OpenScope program, we have established a multi-lab collaboration where individual labs will share sub-components of the stimulus sets but have flexibility in targeting brain areas and recording methods.

Collaborating laboratories include:
- **Bastos lab**: Primate data recordings
- **Najafi and Ruediger labs**: Temporal jittered data recordings across inhibitory cell types and visual areas
- **Podgorski lab**: Dendritic recording with voltage imaging
- **Oweiss lab**: Calcium and voltage imaging with BCI and optogenetics

## Analysis Plan

Our analysis will address three main scientific hypotheses:

### I. Information Encoded by Mismatch Responses

We will determine whether mismatch responses represent:
- Multiplicative novelty (stimulus-specific enhancement for novel stimuli)
- Additive novelty (a generalized "alert" signal)
- Subtractive novelty (the difference between expected vs. actual stimulus)

### II. Categories of Predictions Made by Neurons

We will distinguish between:
- Detailed predictions about the identity of upcoming stimuli
- Deviation of stimulus probability from the expected stimulus ensemble

### III. Mismatch Responses Across Different Types of Predictions

We will compare responses across different prediction paradigms to determine whether there are distinct circuit mechanisms for different types of predictions.

## Expected Outcomes and Significance

This experimental plan will:
1. Collect the first comprehensive set of neuronal data enabling direct comparison across different mismatch error signals
2. Resolve alternative hypotheses regarding unified vs. distinct mechanisms of predictive processing
3. Provide a pivotal resource for validating computational models across multiple mismatch types
4. Advance our understanding of predictive processing in the brain

For more detailed information about specific analysis techniques and methodologies, please refer to the [original paper](https://arxiv.org/abs/2504.09614).