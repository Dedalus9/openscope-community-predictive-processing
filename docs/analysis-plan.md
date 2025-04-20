# Analysis Plan

This document outlines the comprehensive analysis plan for the OpenScope Predictive Processing Project. It describes the methods and approaches we'll use to analyze neural data collected across different experimental paradigms to understand predictive processing mechanisms in the brain.

## Overview

Our analysis is structured to address three main scientific questions, each focusing on different aspects of how the brain implements predictions and processes prediction errors:

1. **What kind of information is encoded by mismatch responses?**
2. **What categories of predictions are made by neurons?**
3. **How do mismatch responses differ across prediction types?**

These questions are designed to help distinguish between competing hypotheses about whether predictive processing relies on a unified neural mechanism or multiple specialized mechanisms.

## I. What kind of information is encoded by mismatch responses?

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

## II. Distinguish between two categories of prediction made by neurons

We will distinguish between two fundamental categories of neural prediction:

- **Detailed stimulus predictions**: Specific predictions about the identity of upcoming stimuli
    - Analysis method: Compare responses to the same mismatch stimulus across closed-loop vs. open-loop conditions
    - Key questions: Do neurons encode precise predictions about what the next stimulus will be?
    - Implementation: Measure neural responses during the sensorimotor mismatch paradigm, comparing closed-loop (when running controls visual flow) vs. open-loop conditions
    - Expected results: Stronger mismatch responses in closed-loop conditions would indicate detailed prediction encoding, as only this condition allows for precise stimulus predictions

- **Ensemble probability deviations**: Detection of stimuli that deviate from the expected statistical ensemble (often described as "adaptation")
    - Analysis method: Population decoding and mutual information analyses comparing control vs. open-loop conditions
    - Key questions: Do neurons primarily signal when stimuli deviate from the expected distribution rather than predicting specific stimuli?
    - Implementation: Calculate mutual information and use machine learning decoders (SVM) to quantify how well neural activity represents individual mismatch stimuli vs. novelty detection
    - Expected results: Greater information content in control vs. open-loop conditions would support ensemble deviation encoding over detailed predictions

- **Predictive learning dynamics**: Emergence of prediction signals with experience
    - Analysis method: Track changes in neural responses to repeated oddball stimuli over time
    - Key questions: Do neural responses adapt as the brain learns stimulus correlations?
    - Implementation: Apply exponential/linear decay models to neuronal responses across trials; use tensor component analysis to identify population-level learning patterns
    - Expected results: Progressive response changes would indicate predictive learning, while static responses would suggest fixed stimulus tuning

- **Pattern completion mechanisms**: Predictive activity during stimulus omissions
    - Analysis method: Analyze neural activity during stimulus omission periods
    - Key questions: Does neural activity during omissions reflect predictions based on preceding context?
    - Implementation: Determine whether omission responses systematically depend on preceding stimulus patterns
    - Expected results: Context-dependent omission responses would indicate predictive pattern completion

These analyses will help us determine whether neural activity primarily represents precise stimulus predictions or statistical regularities, and how these mechanisms develop with experience.

## III. Mismatch responses across different types of predictions

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

## References

1. [Neural mechanisms of predictive processing: a collaborative community experiment through the OpenScope program](https://arxiv.org/abs/2504.09614)