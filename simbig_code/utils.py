"""
Functions adapted from the SimBIG repository (https://github.com/changhoonhahn/simbig).
"""

import h5py
import os
import numpy as np 
import nbodykit.lab as NBlab
from astropy.stats import scott_bin_width


def rh5_hodcatalog(fhod): 
    ''' read NBlab.ArrayCatalog from hdf5 file
    '''
    f = h5py.File(fhod, 'r')
    
    # read in columns
    hod = {}
    for k in f.keys(): 
        if k not in ['cosmo', 'gal_types']: 
            hod[k] = f[k][...]
    
    gals = NBlab.ArrayCatalog(hod)
    
    # save attributes
    for k in f.attrs.keys(): 
        gals.attrs[k] = f.attrs[k]

    gals.attrs['cosmo'] = {}
    for k in f['cosmo'].attrs.keys(): 
        gals.attrs['cosmo'][k] = f['cosmo'].attrs[k]
    
    gals.attrs['gal_types'] = {}
    for k in f['gal_types'].attrs.keys(): 
        gals.attrs['gal_types'][k] = f['gal_types'].attrs[k]

    f.close() 

    # define cosmology; caution: we don't match sigma8 here 
    cosmo = NBlab.cosmology.Planck15.clone(
            h=gals.attrs['h'], 
            Omega0_b=gals.attrs['Ob'], 
            Omega0_cdm=gals.attrs['Om'] - gals.attrs['Ob'],
            m_ncdm=None, 
            n_s=gals.attrs['ns'])

    gals.cosmo = cosmo 
    return gals

def fiducial_cosmology():
    ''' hardcoded fiducial cosmology. This is equivalent to the fiducial cosmology 
    of Quijote. This cosmology is meant to be used for calculating galaxy observables.

    Returns
    -------
    cosmo : nbodykit.lab.cosmology object
        cosmology object with the fiducial cosmology 
    '''
    Om, Ob, h, ns, s8 = 0.3175, 0.049, 0.6711, 0.9624, 0.834

    cosmo = NBlab.cosmology.Planck15.clone(
                h=h,
                Omega0_b=Ob,
                Omega0_cdm=Om - Ob,
                m_ncdm=None,
                n_s=ns)
    return cosmo

def additional_selection(ra, dec, z):
    ''' any additioanl selections that are applied to the forward model and the data 
    '''
    zmin, zmax = 0.45, 0.6
    in_select = (z > zmin) & (z < zmax) & ((ra < 28) | (ra > 335)) & (dec > -6)
    return in_select

def BOSS_randoms(boss_gals, data_dir, weights=None): 
    ''' given forward modeled galaxy catalog (output from the BOSS function) construct 
    accompanying random catalog. 

    Parameters 
    ----------
    boss_gals : catalog object
        catalog output from `forwardmodel.BOSS` function 
    weights : array_like
        corresponding weights for the galaxy catalog
    sample : string
        specify which BOSS sample. currently only supports 'lowz-south'
    veto : boolean
        if True, veto mask is applied on the random 

    Returns
    -------
    nbodykit.ArrayCatalog with RA, DEC, and Z of random catalog

    '''
    frand = os.path.join(data_dir, 'random_DR12v5_CMASS_South.veto.hdf5')
    
    # read RA and Dec values 
    rand = h5py.File(frand, 'r') 
    rand_ra     = rand['ra'][...]
    rand_dec    = rand['dec'][...]

    # generate redshifts that match input galaxy redshift distribution. This 
    # implementation is similiar to the implementation in nbodykit 
    w, bins = scott_bin_width(np.array(boss_gals['Z']), return_bins=True)
    hist, edges = np.histogram(np.array(boss_gals['Z']), bins=bins, weights=weights) 
    cutoffs = np.cumsum(hist) / np.sum(hist)

    prng = np.random.uniform(size=len(rand_ra))
    rand_z = edges[:-1][cutoffs.searchsorted(prng)] + w * np.random.uniform(size=len(rand_ra))

    # further selection functions
    in_select = additional_selection(rand_ra, rand_dec, rand_z)

    return NBlab.ArrayCatalog({'RA': rand_ra[in_select], 'DEC': rand_dec[in_select], 'Z': rand_z[in_select]})
