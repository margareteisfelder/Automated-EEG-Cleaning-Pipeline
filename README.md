# Automated-EEG-Cleaning-Pipeline
Automated pipeline in EEGLab for the batch processing of EEG datasets that filters and removes noisy channels and EOG, EMG, and EKG artifacts, as well as extracts spectral characteristics from all channels. 

## Pipeline Structure 
1. Load raw datasets into Matlab and save in EEGLab toolbox​
2. High-pass filter data at 0.1 Hz​
3. Remove bad channels and re-common average references dataset for significant noise reduction with PREP Pipeline [1] ​
4. Remove line noise at 50/60 Hz with Zapline toolbox ​
5. Run independent component analysis (ICA) with AAR of EOG and EMG using blind source separation (BSS) ​
6. Artifact/channel rejection using Artifact Subspace Recognition (ASR) algorithm
7. Perform Welch's FFT with outputted data
8. Apply FOOOF algorithm to extract aperiodic and periodic components of spectrum and spectral exponent [2] 

## Resources
Loading .eeg files:
https://github.com/arnodelorme/bva-io/blob/master/pop_loadbv.m 
Zapline Toolbox:
https://github.com/MariusKlug/zapline-plus/wiki/Zapline-plus-user-guide#using-the-tool
List of EEGLab Plugins:
https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php
FOOOF Overview and Tools: 
https://fooof-tools.github.io/fooof/
https://fooof-tools.github.io/fooof/generated/fooof.FOOOF.html#fooof.FOOOF.plot
Prep Pipeline: 
https://github.com/VisLab/EEG-Clean-Tools

## References
1. Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M and Robbins KA (2015) The PREP pipeline: standardized preprocessing for large-scale EEG analysis Front. Neuroinform. 9:16. doi: 10.3389/fninf.2015.00016
2. Donoghue T, Haller M, Peterson EJ, Varma P, Sebastian P, Gao R, Noto T, Lara AH, Wallis JD, Knight RT, Shestyuk A, Voytek B (2020). Parameterizing neural power spectra into periodic and aperiodic components. Nature Neuroscience, 23, 1655-1665. DOI: 10.1038/s41593-020-00744-x
