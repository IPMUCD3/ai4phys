""" How to read the 2D maps in the CAMELS multifield data set """

import numpy as np

# Provided are IllustrisTNG and SIMBA
# These are two different hydrodynamic simulation codes
# Others can be downloaded from the CAMELS website if necessary
simcode = 'IllustrisTNG'

# We provide two fields, total matter (Mtot) and pressure (P)
# The pressure can be used as a proxy for the Sunyaev-Zel'dovich effect
# and at a qualitative level is more biased than total matter density.
field = 'Mtot'

# The parameter values corresponding to the simulations
# Each array has 1,000 elements
# Omega_m and sigma_8 are the cosmological parameters (matter density and clustering amplitude)
# SN* are the supernova feedback parameters, AGN* the active galactic nuclei feedback parameters
# Note that the meaning of these parameters (and their effect)
#   differs between the different simulation codes.
# The simulations are arranged in a latin hypercube (LH), so the parameter values are quasi-random.
Omega_m, sigma_8, SN1, AGN1, SN2, AGN2 = np.loadtxt(f'params_LH_{simcode}.txt', unpack=True)

# The 2D images
# 1st dimension corresponds to parameter values,
# 2nd dimension are different maps for a given simulation,
# 3rd and 4th dimension are the image dimensions
imgs = np.load(f'Maps_{field}_{simcode}_LH_z=0.00.npy').reshape(1000, 15, 256, 256)
