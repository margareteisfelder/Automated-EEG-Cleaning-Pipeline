# Automated-EEG-Cleaning-Pipeline
Automated pipeline in EEGLab for the batch processing of EEG datasets that filters and removes noisy channels and EOG, EMG, and EKG artifacts, as well as extracts spectral characteristics from all channels. 

## Pipeline Structure 
1. Load raw datasets into Matlab and save in EEGLab toolbox​
2. High-pass filter data at 0.1 Hz​
3. Remove bad channels and re-common average references dataset for significant noise reduction with PREP Pipeline [1] ​
4. Remove line noise at 50/60 Hz with Zapline toolbox ​
5. Run independent component analysis (ICA) with AAR of EOG and EMG using blind source separation (BSS) ​
6. Artifact/channel rejection using Artifact Subspace Recognition (ASR) algorithm starting threshold 10 with goal of retaining >25% of total data (ex. 30 seconds of usable data from a low quality 2-minute recording)​
7. Perform Welch's FFT with outputted data
8. Apply FOOOF algorithm to extract aperiodic and periodic components of spectrum and spectral exponent [2] 
  
## References
1. Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M and Robbins KA (2015) The PREP pipeline: standardized preprocessing for large-scale EEG analysis Front. Neuroinform. 9:16. doi: 10.3389/fninf.2015.00016
2. Donoghue T, Haller M, Peterson EJ, Varma P, Sebastian P, Gao R, Noto T, Lara AH, Wallis JD, Knight RT, Shestyuk A, Voytek B (2020). Parameterizing neural power spectra into periodic and aperiodic components. Nature Neuroscience, 23, 1655-1665. DOI: 10.1038/s41593-020-00744-x
