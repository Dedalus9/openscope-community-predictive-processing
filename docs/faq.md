# Frequently Asked Questions (FAQ)

This page addresses common questions about the OpenScope Community Predictive Processing project, its data, and how to get involved.

## General Project Questions

### What is the OpenScope Community Predictive Processing project?
The OpenScope Community Predictive Processing project is a collaborative effort to investigate the neural mechanisms underlying predictive processing in the brain. Through carefully designed experiments using in-vivo two-photon imaging and electrophysiological recordings, the project aims to test whether mismatch stimuli engage shared or distinct mechanisms. For a comprehensive overview, see our [arXiv paper](https://arxiv.org/abs/2504.09614).

### Who is involved in this project?
The project involves researchers from multiple institutions, including the Allen Institute and various collaborating laboratories (Bastos lab, Najafi lab, Ruediger lab, and Oweiss lab). We also welcome contributions from the broader research community.

### What are the main research questions?
The project addresses several key questions:
            1. Do temporal, motor, and omission mismatch stimuli engage shared or distinct neural mechanisms?
            2. How do these mechanisms differ across species (mice vs. primates)?
            3. What computational primitives (stimulus adaptation, dendritic computation, E/I balance, hierarchical processing) are central to predictive processing?

## Data and Resources

### How can I access the experimental data?
Specific access instructions and links will be provided on this website as datasets become available.

### What types of data are being collected?
The project collects several types of data:
            - Two-photon calcium imaging data from pan-excitatory and pan-inhibitory lines
            - Neuropixels recordings with SST-optotagging
            - Voltage imaging recordings of pyramidal cell somata and dendrites
            - Behavioral data (running speed, eye movements)

### In what format are the data stored?
Data are standardized in Neurodata Without Borders (NWB) format to ensure interoperability and ease of use across the research community.

### Are there code samples for working with the data?
Yes, we will provide example scripts in the [`code/data-access`](https://github.com/AllenNeuralDynamics/openscope-community-predictive-processing/tree/main/code/data-access) directory of our GitHub repository. These scripts demonstrate how to load, preprocess, and visualize the data.

## Getting Involved

### How can I contribute to the project?
There are several ways to contribute:
            1. Analyze existing datasets and share your findings
            2. Develop or validate computational models using our data
            3. Contribute to the codebase for data analysis or visualization
            4. Conduct complementary experiments in your own lab

See the [How to Contribute](how_to_contribute.md) page for more details.

### How do I report issues or suggest improvements?
Issues can be reported on our [GitHub Issues page](https://github.com/AllenNeuralDynamics/openscope-community-predictive-processing/issues). For discussions and suggestions, please use our [GitHub Discussions](https://github.com/AllenNeuralDynamics/openscope-community-predictive-processing/discussions/21).

### How do I cite this project in my publications?
Please cite our [arXiv paper](https://arxiv.org/abs/2504.09614) when using data or code from this project:

## Technical Questions

### What stimulus paradigms are used in the experiments?
Four main experimental paradigms are used:
            1. **Standard Mismatch**: Drifting gratings with occasional orientation changes
            2. **Sensorimotor Mismatch**: Closed-loop visuo-motor interactions with occasional mismatches
            3. **Sequence Mismatch**: Learned sequences with occasional disruptions
            4. **Temporal Mismatch**: Stimuli with unexpected timing changes

### What hardware is used for the recordings?
The project uses three primary recording systems:
            1. SLAP2 (Scanned Line Angular Projection) for high-speed subcellular imaging
            2. Neuropixels probes for high-density electrophysiological recordings
            3. Mesoscope for wide-field calcium imaging

See the [Hardware Documentation](hardware-overview.md) for more details.

### How are the stimuli implemented?
All stimuli are implemented using the Bonsai framework. The stimulus code is available in the [`code/stimulus-control/src`](https://github.com/AllenNeuralDynamics/openscope-community-predictive-processing/tree/main/code/stimulus-control/src) directory of our GitHub repository. See the [Bonsai Instructions](stimuli/bonsai_instructions.md) for more information.