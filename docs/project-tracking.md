# 🧠 Predictive Processing Project Tracking

This document tracks the progress and key aspects of our Predictive Processing project, which involves the collection and analysis of new data related to the neural mechanisms of predictive processing.

---

## Project Management Workflow

We use a [GitHub Kanban board](https://github.com/orgs/AllenNeuralDynamics/projects/149/views/1) to track individual tickets and provide visibility into the progress of the project. The board organizes tickets added to the repository and follows a standard workflow.

### Workflow Overview:
1. **Create a GitHub Issue**:
    - Each task or deliverable should be created as a GitHub issue in the repository.
    - Clearly define the task, its scope, and any relevant details.
    - Provide estimated start and end dates, to be updated as the project progresses.
    - Assign the issue to the appropriate team member(s) and indicate the Laboratory that will be performing the task.
    - Use labels to categorize issues (e.g., `data-analysis`, `stimulus-design`, `documentation`).

2. **Track on the Kanban Board**:
    - All issues are automatically added to the [Kanban board](https://github.com/orgs/AllenNeuralDynamics/projects/149/views/7).
    - The board is organized into columns representing different stages of the workflow:
        - **To Do**: Tasks that are planned but not yet started.
        - **In Progress**: Tasks currently being worked on.
        - **Review**: Tasks that are completed and awaiting review.
        - **Done**: Tasks that are completed and approved.

3. **Update Regularly**:
    - Team members should update the status of their issues on the Kanban board as they progress through the workflow.
    - Add comments to issues to provide updates or request feedback.

---

## A. Data Collection and Stimulus Design

**🎯 Title & Goal:**  
*Design and implement stimuli for investigating predictive processing mechanisms across multiple experimental paradigms.*

**👥 Contributors:**  
*Jerome Lecoq, Carter, Maedeh, Kaspar*

**📝 Description:**  
This project focuses on developing and implementing four key experimental paradigms to investigate different aspects of predictive processing:
 
1. **Standard Mismatch**: Habituating animals to drifting gratings of the same orientation with occasional mismatch stimuli
2. **Sensorimotor Mismatch**: Establishing closed-loop visuo-motor interactions with occasional mismatches
3. **Sequence Mismatch**: Testing responses to disruptions in learned sequences of stimuli
4. **Temporal Mismatch**: Investigating responses to unexpected timing changes in sensory inputs

Each stimulus paradigm is implemented in Bonsai and includes appropriate control conditions to isolate specific predictive mechanisms.

**Progress:**
- ✅ Standard oddball and sensorimotor oddball stimuli implemented in Bonsai
- ✅ Initial SLAP2 recordings completed with mouse #794237 and #787727
- 🔄 Ongoing refinement of temporal mismatch stimuli

---

## B. Data Curation and Sharing

**🎯 Title & Goal:**  
*Ensure all data and metadata are properly curated, formatted, and shared through public repositories.*

**👥 Contributors:**  
*Jerome Lecoq*

**📝 Description:**  
This project focuses on the critical task of data management, ensuring that all datasets are released without embargo, following the community policy.  
This includes standardizing data in NWB format, uploading datasets to the Allen Institute or DANDI/NWB archives, and providing comprehensive documentation.

 Key data types include:
 - Two-photon calcium imaging data from pan-excitatory and pan-inhibitory lines
 - Neuropixels recordings with SST-optotagging
 - Voltage imaging recordings of pyramidal cell somata and dendrites

---

## C. Single Neuron Analysis

**🎯 Title & Goal:**  
*Analyze how individual neurons encode prediction errors across different mismatch paradigms.*

**👥 Contributors:**  
*Seeking contributors*

**📝 Description:**  
This project investigates how individual neurons respond to expected versus unexpected stimuli across different prediction paradigms. The analysis will determine:
 
1. **Information Encoded by Mismatch Responses**:
    - Multiplicative novelty (stimulus-specific enhancement)
    - Additive novelty (generalized "alert" signal)
    - Subtractive novelty (difference between expected vs. actual stimulus)

2. **Response Characteristics**:
    - Response amplitude, latency, and duration
    - Comparison across cell types (excitatory vs. inhibitory populations)
    - Layer-specific differences in response properties

3. **Predictive Timing Analysis**:
    - Characterizing responses to temporal mismatch stimuli
    - Evaluating how neurons encode specific temporal predictions

**Analysis Methods:**
- Event-triggered averaging for calcium imaging data
- Peri-stimulus time histograms for Neuropixels data
- Bootstrap resampling for statistical validation
- Comparative analysis across multiple mismatch paradigms

---

## D. Population Dynamics and Decoding

**🎯 Title & Goal:**  
*Investigate population-level encoding of predictions and prediction errors.*

**👥 Contributors:**  
*Seeking contributors*

**📝 Description:**  
This project aims to understand how populations of neurons collectively represent and process predictions.

1. **Decoding Analysis**:
    - Quantify information encoded about novelty per se versus specific stimulus identity
    - Compare decoding performance across different brain regions and layers
    - Evaluate the temporal evolution of population codes during prediction formation

2. **Dimensionality Reduction**:
    - Apply techniques like PCA, t-SNE, and UMAP to visualize population activity
    - Identify latent variables corresponding to predictions and prediction errors
    - Track changes in neural manifold structure over repeated presentations

3. **Cross-Paradigm Comparison**:
    - Compare population responses across standard, sensorimotor, and sequence mismatch paradigms
    - Determine whether distinct or overlapping neural populations encode different types of predictions

**Analysis Methods:**
- Linear and nonlinear decoding algorithms (SVMs, neural networks)
- Tensor Component Analysis (TCA) for extracting trial-dependent dynamics
- Mutual information calculations
- Visualization of geometric structure of population activity

---

## E. Computational Modeling of Predictive Processing

**🎯 Title & Goal:**  
*Develop and validate computational models that integrate multiple predictive mechanisms.*

**👥 Contributors:**  
*Seeking contributors*

**📝 Description:**  
This project involves creating and testing computational models that simulate and explain the neural processes underlying predictive processing.

1. **Model Development**:
    - Integrate key computational primitives:
      - Stimulus adaptation
      - Dendritic computation
      - Excitatory/inhibitory balance
      - Hierarchical processing
    - Implement models that can account for responses across different mismatch paradigms

2. **Model Validation**:
    - Fit models to experimental data from multiple mismatch paradigms
    - Quantitatively compare models in terms of their ability to account for the patterns of neuronal activity
    - Test model predictions on held-out data

 3. **Mechanistic Studies**:
    - Use models to determine the relative contributions of different predictive mechanisms
    - Simulate the effects of manipulating specific circuit components
    - Explore how predictions at different timescales interact

**Analysis Methods:**
- Deep learning models using self-supervised learning
- Information theory criteria and cross-validation techniques
- Parameter fitting and model comparison
- Simulations of neural network dynamics

---

## Questions and Feedback

If you have any questions or need clarification about the project tracking workflow or tasks, feel free to post them in our [GitHub Discussions](https://github.com/AllenNeuralDynamics/openscope-community-predictive-processing/discussions/21).
