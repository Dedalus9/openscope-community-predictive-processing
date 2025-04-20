This repository stores Bonsai code to run visual stimuli that are part of this community effort: [Neural mechanisms of predictive processing](https://arxiv.org/abs/2504.09614).

## Organization

All Bonsai workflows should go into the [`code/stimulus-control/src`](https://github.com/AllenNeuralDynamics/openscope-community-predictive-processing/tree/main/code/stimulus-control/src) folder, along with the `Extensions` folder.

## Deployment

To deploy the Bonsai code, run [`code/stimulus-control/bonsai/setup.cmd`](https://github.com/AllenNeuralDynamics/openscope-community-predictive-processing/blob/main/code/stimulus-control/bonsai/setup.cmd).  
This small script will download and regenerate the current Bonsai environment ([see tutorial for further details](https://bonsai-rx.org/docs/articles/environments.html)).  
Each time you change a project dependency via the `Package Manager`, the `Bonsai.Config` file will be updated, and you can choose to commit these changes.

---

## Prerequisites

These should only need to be installed once on a fresh new system and are not required if simply refreshing the install or deploying to a new folder.

- **Operating System**: Windows 10 or 11
- **Tools**:
    - [Visual Studio Code](https://code.visualstudio.com/) (highly recommended for editing code scripts and Git commits)
    - [Git for Windows](https://gitforwindows.org/) (highly recommended for cloning and manipulating this repository)
    - [.NET Framework 4.7.2 Developer Pack](https://dotnet.microsoft.com/download/dotnet-framework/thank-you/net472-developer-pack-offline-installer) (required for IntelliSense when editing code scripts)
    - [Visual C++ Redistributable for Visual Studio 2012](https://www.microsoft.com/en-us/download/details.aspx?id=30679) (native dependency for OpenCV)

### Hardware Specific:
These are needed to run Bonsai workflows on the Allen Institute rigs with HARP devices:
- [FTDI CDM Driver 2.12.28](https://www.ftdichip.com/Drivers/CDM/CDM21228_Setup.zip) (serial port drivers for HARP devices)
- [Spinnaker SDK 1.29.0.5](https://www.flir.co.uk/support/products/spinnaker-sdk/#Downloads) (device drivers for FLIR cameras)
    - On the FLIR website: `Download > Archive > 1.29.0.5 > SpinnakerSDK_FULL_1.29.0.5_x64.exe`
- [NI-DAQmx 19.0](https://www.ni.com/en-gb/support/downloads/drivers/download.ni-daq-mx.html#301173) (drivers for NI-DAQ devices)

---

## Related Documents

- **[Experimental Plan](../experimental-plan.md)**: Overview of experimental paradigms using these stimuli
- **[Standard Oddball Stimulus](standard-oddball.md)**: Details of the standard oddball paradigm implementation
- **[Sensory-Motor Closed-Loop](sensory-motor-closed-loop.md)**: Information about sensorimotor paradigm implementation
- **[List of Bonsai Scripts](list_scripts.md)**: Catalog of all available stimulus scripts