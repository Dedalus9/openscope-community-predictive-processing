# Detailed Experimental Plan

This document provides a comprehensive experimental plan for investigating neural mechanisms of predictive processing as part of the OpenScope community project. The plan is designed to resolve existing conflicts between experimental and theoretical domains and deepen our understanding of the neural circuits underlying predictive processing.

## Background and Scientific Context

### Current State of Predictive Processing Research

Predictive processing theories propose that the brain continuously builds and updates internal models of the world, using these models to predict incoming sensory signals. When predictions differ from actual inputs, the resulting prediction errors drive learning and perceptual updating. However, significant questions remain about how these processes are implemented in neural circuits.

Recent research has revealed that the brain may employ various mechanisms for predictive processing, which can differ depending on:
- The sensory modality (visual, auditory, somatosensory)
- The type of prediction being made (spatial, temporal, sensorimotor)
- The complexity and timescale of the prediction
- The species and brain region involved

Our review of the literature has identified several key computational primitives that may support predictive processing:

1. **Stimulus adaptation**: Neurons adjust their responses to recurring stimuli, potentially enhancing sensitivity to change
2. **Dendritic computation**: Integration of top-down and bottom-up inputs within a neuron's dendrites may support prediction error calculation
3. **Excitatory/inhibitory (E/I) balance**: Different inhibitory interneuron subtypes provide a framework for complex predictions and error signaling
4. **Hierarchical processing**: Multi-level processing across brain areas enables sophisticated, multi-modal predictions

### Evidence for Distinct Mechanisms

Current evidence suggests that mechanisms of predictive processing differ across paradigms:

- In visual oddball paradigms, prediction errors are predominantly found in layer 2/3 pyramidal neurons
- In auditory sensorimotor paradigms, mismatch responses occur in both layer 5 and layer 2/3
- In somatosensory oddball paradigms, prediction errors have been identified primarily in layer 4 and layer 6
- Layer-specific responses differ across species, with shallower hierarchical organization in mice compared to primates

These divergent findings highlight the need for a systematic investigation using comparable methods across prediction paradigms.

## Key Research Questions and Hypotheses

### Primary Research Questions

1. Do sequential, sensory-motor, and omission mismatch stimuli engage shared or distinct neural mechanisms?
2. How do these mechanisms differ across cortical layers, cell types, and brain regions?
3. Are prediction errors computed locally within a brain area or distributed across multiple areas?
4. How do predictive processing mechanisms differ between mice and primates?

### Alternative Hypotheses

We are testing two alternative hypotheses:

- **H0 (Multiple Mechanisms)**: Different types of prediction errors involve fundamentally distinct neural mechanisms, with specialized circuits for each type of mismatch processing.
- **H1 (Unified Mechanism)**: A common computational principle underlies all mismatch responses, with apparent differences reflecting implementation variations rather than distinct mechanisms.

## Experimental Design

### 1. Comprehensive Stimulus Set Design

To systematically investigate different aspects of predictive processing, we've designed a stimulus set that includes several validated mismatch stimuli capable of engaging different neural mechanisms:

#### Stimulus Types

All experiments will feature sequences of drifting gratings with five types of oddball events:

1. **Orientation Oddballs**: Unexpected changes in grating orientation
   - Standard: 0° orientation drifting gratings
   - Deviant: 90° or 45° orientation drifting gratings
   - Ratio: 120:1 (standard:deviant)

2. **Motion Oddballs**: Unexpected changes in drift direction or speed
   - Standard: Consistent motion parameters
   - Deviant: Reversed or halted motion
   - Ratio: 120:1 (standard:deviant)

3. **Omission Oddballs**: Complete absence of expected stimulus
   - 5% probability of stimulus omission
   - Never occurs during a stimulus change or preceding a change

4. **Temporal Oddballs**: Unexpected timing of stimulus presentation
   - Standard: 250ms stimulus duration, 500ms ISI
   - Deviant: 150ms or 350ms stimulus duration
   - Blocks alternate between fixed and jittered timing

5. **Sensorimotor Oddballs**: Unexpected sensory feedback during motor activity
   - Standard: Visual flow coupled to running speed
   - Deviant: Flow faster/slower than expected based on running speed
   - Implemented during active running periods

### 2. Session Structure and Paradigms

These oddball stimuli will be presented in three different paradigms, each designed to engage different prediction mechanisms as described in our review paper "Neural mechanisms of predictive processing: a collaborative community experiment through the OpenScope program":

#### Paradigm 1 – Sequential Mismatch (Standard Oddball Sequence)

- Animals presented with series of drifting gratings (same orientation)
- Occasional oddball stimuli (orientation changes, omissions)
- Passive viewing condition
- Duration: 60 minutes (includes 10-minute habituation)
- 8 repetitions of each oddball type
- Tests predictions based on sequential patterns

#### Paradigm 2 – Sensory-Motor Mismatch (Sensorimotor Coupling)

- Animals run on wheel with visual flow coupled to movement
- Closed-loop visuo-motor coupling (running controls visual flow)
- Occasional mismatches between running and visual flow
- Same oddball types as Session 1
- Duration: 60 minutes (includes 10-minute habituation)
- Tests predictions based on self-generated sensory consequences

#### Paradigm 3 – Omission Mismatch

- Focus on the absence of expected stimuli
- Trials with regular stimulus presentation (establish expectation)
- 5% probability of stimulus omission
- Duration: 60 minutes (includes 10-minute habituation)
- Tests predictions based on temporal expectations

#### Additional Session Types

In addition to the three core paradigms, we will conduct specialized sessions to further investigate temporal aspects of prediction:

**Complex Sequence Learning**
- Animals habituated to specific sequences of 4 stimuli
- Sequences repeat once per second for 37 minutes
- Oddball stimuli introduced in third position of sequence
- Controls for context-dependent prediction
- Duration: 60 minutes (includes 20-minute habituation)

**Temporal Prediction**
- Focus on timing predictability rather than stimulus identity
- Alternating blocks of fixed vs. jittered timing
- Shorter/longer duration stimuli serve as temporal oddballs
- Duration: 60 minutes (includes 10-minute habituation per block)

### 3. Recording Approaches

To evaluate the relative contributions of different mechanisms, we will use three complementary recording approaches:

#### SLAP2 Two-Photon Imaging

- Ultra-fast subcellular imaging (220 Hz)
- Targeted recording of dendrites and somata simultaneously
- Cell-type specific targeting through transgenic mouse lines:
  - Slc17a7-IRES2-Cre for excitatory neurons
  - Sst-IRES-Cre for somatostatin inhibitory neurons
  - Vip-IRES-Cre for VIP inhibitory neurons
- Allows direct investigation of apical dendrite contributions
- Specific objectives:
  - Determine whether prediction errors are computed at the level of single neurons
  - Test whether top-down predictions and bottom-up inputs are integrated in specific dendritic compartments
  - Examine how inhibitory interneurons shape prediction error signals

#### Neuropixels Recordings

- High-density electrophysiological recordings (384 channels)
- Millisecond-precision spike timing
- Simultaneous recording across cortical layers and areas
- Implementation of optogenetic tagging for cell-type identification
- Coverage of multiple regions in a single recording
- Specific objectives:
  - Compare response latencies across areas to determine signal flow direction
  - Evaluate layer-specific responses across different prediction paradigms
  - Investigate oscillatory synchronization during prediction and error states

#### Mesoscope Imaging

- Dual-beam technology for multi-plane imaging
- Simultaneous recording from 4 depths across 2 areas
- 11 Hz per plane imaging rate
- Tracking same neural populations across sessions
- Coverage of multiple visual areas (V1 and higher areas)
- Specific objectives:
  - Examine inter-area coordination during prediction and error signaling
  - Determine whether common neural ensembles participate in different prediction paradigms
  - Track changes in prediction signals over multiple sessions

### 4. Experimental Subjects and Brain Regions

#### Mice

- Number: 82 mice across all recording methods
- Mouse lines:
  - Excitatory neurons: Slc17a7-IRES2-Cre × Ai93 or Ai148
  - Inhibitory neurons: Sst-IRES-Cre × Ai93, Vip-IRES-Cre × Ai148
- Brain regions:
  - Primary visual cortex (V1)
  - Secondary visual areas (LM, AL)
  - Motor cortex (M1, M2)
  - Prefrontal regions

#### Primates (Collaborative Studies)

- Non-human primates (macaques)
- Comparable visual oddball and prediction paradigms
- Brain regions:
  - V1, V2, V4
  - MT/MST
  - Prefrontal regions

### 5. Experimental Timeline

Each mouse will undergo:
- Habituation and task training (2-3 weeks)
- Cranial window implantation and recovery
- Intrinsic signal imaging for area identification
- Multiple recording sessions (one session type per day)
- SLAP2/Mesoscope: 8-10 sessions per mouse
- Neuropixels: 4-6 sessions per mouse

## Analysis Plan

This document focuses on the experimental design. For our detailed analysis approach, please see the [Analysis Plan](analysis-plan.md) document, which covers:

1. What kind of information is encoded by mismatch responses
2. Distinguishing between categories of predictions made by neurons
3. Comparing mismatch responses across different types of predictions
4. Computational modeling approaches

For a more concise overview of our approach, see the [Experimental Plan](experimental-plan.md).

## Expected Outcomes and Significance

This experimental plan will produce:

1. The first comprehensive dataset enabling direct comparison across different mismatch error signals
2. Resolution between alternative hypotheses regarding unified vs. distinct mechanisms
3. A detailed map of how prediction errors are encoded across cell types, layers, and regions
4. A pivotal resource for validating computational models of predictive processing

The resulting datasets, collected through the OpenScope program, will be shared openly with the neuroscience community via NWB files on the DANDI archive. This approach will enable model validation and community analysis, fostering iterative refinement of our understanding of the neural mechanisms underlying predictive processing.

## References

1. [Neural mechanisms of predictive processing: a collaborative community experiment through the OpenScope program](https://arxiv.org/abs/2504.09614)