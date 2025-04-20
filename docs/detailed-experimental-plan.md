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

Our analysis will address three main scientific questions:

### I. What kind of information is encoded by mismatch responses?

We will determine whether mismatch responses represent:

- **Multiplicative novelty**: Stimulus-specific enhancement for novel stimuli
  - Analysis method: Compare tuning curves between standard and oddball conditions
  - Expected signature: Multiplicative scaling of tuning curves
  - Testable prediction: Neurons with strong preference for the standard stimulus will show the largest mismatch responses to deviants
  - Implementation: Fit tuning curves with multiplicative gain parameters and test for significant changes

- **Additive novelty**: A generalized "alert" signal independent of stimulus identity
  - Analysis method: Test for uniform response increase across all stimulus conditions
  - Expected signature: Constant response increment regardless of stimulus preference
  - Testable prediction: All neurons will show similar magnitude mismatch responses regardless of their tuning
  - Implementation: Fit tuning curves with additive offset parameters and test for significant changes

- **Subtractive novelty**: Difference between expected vs. actual stimulus (true prediction error)
  - Analysis method: Calculate difference between predicted response (based on prior stimuli) and actual response
  - Expected signature: Activity proportional to the difference between predicted and actual stimulus representations
  - Testable prediction: Response will be proportional to distance between expected and actual stimulus in feature space
  - Implementation: Build predictive models of expected neural activity and compare with actual activity

For each of these possibilities, we will compare results across paradigms to test whether the same information coding principles apply consistently to different types of prediction errors.

### II. Distinguish between two categories of prediction made by neurons

We will distinguish between:
- A. Detailed predictions about the identity of the upcoming stimulus
- B. Deviation of stimulus probability from the expected stimulus ensemble, often described in the literature as "adaptation". This empirical outcome could be interpreted as a form of refutation of the hypothesis that predictive computation was involved in the experimental conditions tested.

Analysis #1: Compare the response to the same mismatch stimulus in all three conditions for the sensorimotor mismatch (session 2):
- Is the mismatch response > for closed loop vs. open loop
  - YES indicates that the neuron encodes a detailed prediction (as only the closed loop condition allows a detailed prediction)
- Is the mismatch response > control vs. open loop
  - YES indicates that the neuron encodes deviation from the expected ensemble (as a blank differs more from the mismatch grating than the vertically oriented grating present in the closed loop condition)

Analysis #2: Calculate decoding performance / info encoded for individual mismatch stimuli vs. for novelty per se.
- Use population decoder to identify the occurrence of an individual mismatch stimulus (target) versus all the other neural activity; start with a linear decoder (support vector machine):
  - this quantifies the fidelity for encoding the identity of each of 4 mismatch stimuli
- In a complementary fashion, calculate the mutual information each neuron represents about an individual mismatch stimulus versus all other neural activity
- Similarly, calculate decoding performance and information for a comparison of neural activity during any mismatch stimulus vs all other neural activity;
  - this quantifies the fidelity for encoding stimulus novelty per se
- If significantly more information is encoded in the closed loop condition vs. open loop
  - YES indicates encodes of a detailed prediction
- If significantly more information is encoded in the control condition vs. open loop
  - YES indicates encoding of a deviation from the expected ensemble

Analysis #3: Emergence of Prediction Signals in Single Neurons and Neural Populations
When new, arbitrary correlations are created by the experimenter, the brain must, in principle, learn these new correlations. This can be demonstrated by showing several kinds of changes in neural responses to the same stimuli over time. These changes may occur within a single recording session, which is often interpreted as a form of adaptation, or across recording sessions, which is typically interpreted as learning.

Key Hypothesis Tests:
- Predictive coding vs. static tuning: Do individual neurons or neural populations show changes in their response to the same oddball stimuli?
  - YES indicates evidence of predictive computation
  - NO indicates evidence of static or previously learned tuning to stimuli
- "Predictive" Activity: Do neurons or populations of neurons exhibit activity that systematically depends on what the upcoming stimulus is (as can be demonstrated by changing stimulus contingencies)?
  - YES suggests that the neural activity was in part encoding the identity of the upcoming stimulus
  - NO indicates that the neural activity encodes the identity of the current stimulus
- "Pattern completion" activity: Do neurons or populations of neurons exhibit activity during stimulus omission that depends systematically on the preceding stimulus?
  - YES indicates a form of predictive computation, in which predictions are embodied, in part, by specific neural activity driven by events that predict an upcoming stimulus (rather than by the stimulus itself)
  - NO indicates that a response to the omission itself
- Latent component dynamics: Do identified latent variables exhibit systematic changes over trials?
  - YES indicates evidence of predictive computation revealed only at the population level
- Neural dimensionality reduction: Does the manifold structure of mismatch responses shift toward a more compact, lower-dimensional space with repeated exposure?
  - YES indicates a structure of predictive computation that is consistent with theories about efficient coding and/or maximization of coding capacity
- Conjunctive vs. disentangled representation: Does the visualized geometric structure of population activity embedded in a 3D space; e.g. using unsupervised UMAP (Uniform Manifold Approximation and Projection), show distinct, possibly orthogonal, trajectories that could reveal disentangled coding schemes for different signals (e.g. for stimulus evoked responses vs. prediction errors)?
  - YES indicates that the population neural code can simultaneously represent information about the stimulus as well as its predictive context

Single Neuron Analysis: Determine whether individual neurons exhibit changes in their responses with repeated oddball presentations, indicative of learning.
- Trial-by-Trial Response Analysis: Measure the amplitude and timing of neuronal responses to each oddball stimulus across trials.
- Model Fitting: Apply exponential or linear decay models to these responses to measure trends over time.
- Statistical Validation: Use bootstrap resampling to evaluate the significance of observed changes.
- Time Points for Analysis: Pre-Oddball Baseline Period: A period before the oddball onset (e.g., -200 ms to stimulus onset at 0 ms) to establish baseline activity levels.
- Oddball Response Window: A post stimulus onset interval (e.g., 0 to 300 ms) capturing the immediate neuronal response to the oddball stimulus.

Population Latent Analysis: Identify latent patterns within neural populations that correspond to predictions and prediction error signals.
- Tensor Component Analysis (TCA): Decompose multi-dimensional neural data to uncover components with trial-dependent dynamics.
- Time Points for Analysis: Pre-Oddball Baseline: A period before oddball onset (e.g., -200 ms to stimulus onset at 0 ms) to establish baseline population activity levels.
- Oddball Response Window: The duration of the oddball stimulus presentation (e.g., 0 to 300 ms) capturing immediate population responses to the oddball stimulus.
- Post-Oddball Period: A post stimulus offset interval (e.g., 300 ms to 600 ms) to monitor any sustained or delayed responses.
- Inter-Trial Intervals: Periods between oddball trials to evaluate baseline stability and potential anticipatory activity.

Cross-Day Analysis: Monitor the activity of individual neurons or neural populations over time to identify changes in prediction error signaling and learning processes.

### III. Mismatch responses across different types of predictions

We will compare neural responses across our five experimental paradigms to determine:

- **Shared vs. distinct neural ensembles**:
  - Analysis method: Track the same neurons across multiple paradigms
  - Key questions: Do the same neurons encode different types of prediction errors?
  - Implementation: Apply dimensionality reduction to identify shared response subspaces
  - Expected results: Either consistent neural ensemble involvement across paradigms (supporting unified mechanism) or distinct ensemble recruitment (supporting multiple mechanisms)

- **Mismatch type specificity**:
  - Analysis method: Compare responses to different mismatch types (orientation, motion, temporal, omission)
  - Key questions: Are responses stimulus-feature specific or general across mismatch types?
  - Implementation: Compare population response patterns across mismatch types
  - Expected results: Either similar response patterns across mismatch types (supporting unified mechanism) or stimulus-specific patterns (supporting multiple mechanisms)

- **Passive vs. active prediction differences**:
  - Analysis method: Directly compare oddball vs. sensorimotor mismatch responses
  - Key questions: How do motor-based predictions differ from passive statistical learning?
  - Implementation: Compare response magnitude, timing, and cell-type specificity
  - Expected results: Either similar mechanisms with contextual modulation (unified) or fundamentally different computational mechanisms (multiple)

- **Temporal dynamics analysis**:
  - Analysis method: Compare response onset, duration, and oscillatory patterns across paradigms
  - Key questions: Do different prediction types share temporal signatures?
  - Implementation: Time-frequency analysis of response patterns
  - Expected results: Either consistent temporal dynamics (supporting unified mechanism) or distinct dynamics (supporting multiple mechanisms)

This comprehensive comparison across paradigms will provide critical evidence for evaluating whether the brain implements a unified prediction error mechanism that operates across contexts or employs multiple specialized mechanisms for different types of predictions.

## Computational Modeling

We will develop computational models to formalize hypotheses about predictive processing mechanisms:

1. **Predictive Coding Models**:
   - Implement hierarchical prediction networks with explicit error computation
   - Model distinct error channels for different types of prediction violations
   - Compare model predictions with neural response patterns

2. **Reinforcement Learning Models**:
   - Implement models with prediction error as a teaching signal
   - Focus on learning dynamics during repeated exposure to prediction violations
   - Test whether learning rates differ across prediction types

3. **Dynamical Systems Models**:
   - Create recurrent network models capable of generating predictions
   - Model connectivity structures between excitatory and inhibitory neurons
   - Determine minimal circuit requirements for different types of prediction errors

These models will provide quantitative predictions about neural activity patterns under different hypotheses, which we can test against our experimental data.

## Expected Outcomes and Significance

This experimental plan will produce:

1. The first comprehensive dataset enabling direct comparison across different mismatch error signals
2. Resolution between alternative hypotheses regarding unified vs. distinct mechanisms
3. A detailed map of how prediction errors are encoded across cell types, layers, and regions
4. A pivotal resource for validating computational models of predictive processing

The resulting datasets, collected through the OpenScope program, will be shared openly with the neuroscience community via NWB files on the DANDI archive. This approach will enable model validation and community analysis, fostering iterative refinement of our understanding of the neural mechanisms underlying predictive processing.

## References

1. [Neural mechanisms of predictive processing: a collaborative community experiment through the OpenScope program](https://arxiv.org/abs/2504.09614)