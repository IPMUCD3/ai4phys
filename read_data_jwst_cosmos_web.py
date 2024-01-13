#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 00:52:09 2024

@author: Lilan Yang
"""

from astropy.io import fits
cosmos_cata=fits.open('comosweb_cd3.fits')[1].data
source_id=cosmos_cata['id']
source_ra=cosmos_cata['ra']
source_dec=cosmos_cata['dec']
source_z=cosmos_cata['z']

# #Write files:
# write_file = open('cd3_catalog.txt','w') 

# write_file.write("ID RA Dec\n")
# for i in range(len(source_z)):
#     write_file.write("{0} {1} {2} {3}\n".format(i, source_ra[i], source_dec[i], source_z[i]))
# write_file.close()

#%%

ID=30
#psf data
parent_dir = './'
fits_psf115data=fits.open(parent_dir+"JWST_f115w.psf")[1].data[0][0][0]
fits_psf150data=fits.open(parent_dir+"JWST_f150w.psf")[1].data[0][0][0]
fits_psf277data=fits.open(parent_dir+"JWST_f277w.psf")[1].data[0][0][0]
fits_psf444data=fits.open(parent_dir+"JWST_f444w.psf")[1].data[0][0][0]
#img data
import glob
fits115=glob.glob(parent_dir+"cd3_cutout/{0}_NIRCAM_F115W_cutout*.fits".format(ID))[0]
fits150=glob.glob(parent_dir+"cd3_cutout/{0}_NIRCAM_F150W_cutout*.fits".format(ID))[0]
fits277=glob.glob(parent_dir+"cd3_cutout/{0}_NIRCAM_F277W_cutout*.fits".format(ID))[0]
fits444=glob.glob(parent_dir+"cd3_cutout/{0}_NIRCAM_F444W_cutout*.fits".format(ID))[0]
fits115data=fits.open(fits115)[1].data
fits150data=fits.open(fits150)[1].data
fits277data=fits.open(fits277)[1].data
fits444data=fits.open(fits444)[1].data

#Load the noise map
fits115noise=fits.open(fits115)[3].data
fits150noise=fits.open(fits150)[3].data
fits277noise=fits.open(fits277)[3].data
fits444noise=fits.open(fits444)[3].data

#Plot images and psf
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#images
print("Plot image SCI data")
fig, axes = plt.subplots(1, 4, figsize=(12, 3))
# Plot each image in a separate subplot
axes[0].imshow(fits.open(fits115)[1].data, cmap='gist_heat',  norm=colors.LogNorm(vmin=0.001, vmax=0.5),origin='lower')
axes[0].set_title('ID'+repr(ID)+'_F115W')

axes[1].imshow(fits150data, cmap='gist_heat',  norm=colors.LogNorm(vmin=0.001, vmax=0.5),origin='lower')
axes[1].set_title('ID'+repr(ID)+'_F150W')

axes[2].imshow(fits277data, cmap='gist_heat',  norm=colors.LogNorm(vmin=0.001, vmax=0.5),origin='lower')
axes[2].set_title('ID'+repr(ID)+'_F277W')

axes[3].imshow(fits444data, cmap='gist_heat', norm=colors.LogNorm(vmin=0.001, vmax=0.5),origin='lower')
axes[3].set_title('ID'+repr(ID)+'_F444W')

plt.tight_layout()
plt.show()


#Plot noise map
print("Plot image noise map")
fig, axes = plt.subplots(1, 4, figsize=(12, 3))
# Plot each image in a separate subplot
axes[0].imshow(fits115noise, cmap='gist_heat',origin='lower')
axes[0].set_title('ID'+repr(ID)+'_F115W')

axes[1].imshow(fits150noise, cmap='gist_heat',origin='lower')
axes[1].set_title('ID'+repr(ID)+'_F150W')

axes[2].imshow(fits277noise, cmap='gist_heat',origin='lower')
axes[2].set_title('ID'+repr(ID)+'_F277W')

axes[3].imshow(fits444noise, cmap='gist_heat',origin='lower')
axes[3].set_title('ID'+repr(ID)+'_F444W')

plt.tight_layout()
plt.show()

#psfs
print("Plot the PSF")
fig, axes = plt.subplots(1, 4, figsize=(12, 3))
# Plot each image in a separate subplot
axes[0].imshow(fits_psf115data, cmap='gist_heat',  norm=colors.LogNorm(),origin='lower')
axes[0].set_title('F115W PSF')

axes[1].imshow(fits_psf150data, cmap='gist_heat',  norm=colors.LogNorm(),origin='lower')
axes[1].set_title('F150W')

axes[2].imshow(fits_psf277data, cmap='gist_heat',  norm=colors.LogNorm(),origin='lower')
axes[2].set_title('F277W')

axes[3].imshow(fits_psf444data, cmap='gist_heat', norm=colors.LogNorm(),origin='lower')
axes[3].set_title('F444W')

plt.tight_layout()
plt.show()
