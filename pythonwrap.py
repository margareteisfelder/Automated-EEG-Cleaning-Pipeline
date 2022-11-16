
import numpy as np
import matplotlib
matplotlib.use('QTAgg')
import matplotlib.pyplot as plt
from scipy.io import loadmat, savemat

from fooof import FOOOFGroup

# Load the mat file 
data = loadmat('power_spectrum.mat')

# Unpack data from dictioanry, and squeeze numpy arrays
freqs = np.squeeze(data['freqs']).astype('float')
psds = np.squeeze(data['psds']).astype('float')

# Transpose power spectra, to have the expected orientation for FOOOF
psds = psds.T  

# Initialize FOOOFGroup object
fg = FOOOFGroup()

# Fit the FOOOF model, and report
fg.report(freqs, psds, [1, 30])

# # You can also save out PDF reports of the FOOOFGroup fits, same as with FOOOF
# fg.save_report('FOOOFGroup_report')

# Extract aperiodic parameters
aps = fg.get_params('aperiodic_params')
exps = fg.get_params('aperiodic_params', 'exponent')

# Extract peak parameters
peaks = fg.get_params('peak_params')
cfs = fg.get_params('peak_params', 'CF')

# Extract goodness-of-fit metrics
errors = fg.get_params('error')
r2s = fg.get_params('r_squared')

## Save out fooof results to json file
##  There is a utility file to load this json file directly into Matlab
#fg.save('fooof_results', save_results=True, save_settings=True)

for ind, f_res in enumerate(fg):
    savemat('f_results_' + str(ind) + '.mat', f_res._asdict())
# # Extract a particular spectrum, specified by index
# #  Here we also specify to regenerate the the full model fit, from the results
# fm = fg.get_fooof(ind=0, regenerate=True)
# # Print results and plot extracted model fit
# fm.print_results()
# #fm.plot(plot_peaks='shade', peak_kwargs={'color' : 'green'}) #,plt_log = True)
# #plt.show()
# ap_params, peak_params, r_squared, fit_error, gauss_params = fm.get_results()
# 
# fm = fg.get_fooof(ind=1, regenerate=True)
# # Print results and plot extracted model fit
# #fm.print_results()
# #fm.plot(plot_peaks='shade', peak_kwargs={'color' : 'green'}) #, plt_log = True)
# plt.show()