# a few handy tools when working with icon output files

import numpy as np

def ind_from_latlon(lats,lons,lat,lon,verbose=False):
    """Find the nearest neighbouring index to given location.

    Args:
        lats (2d array):            Latitude grid
        lons (2d array):            Longitude grid
        lat (float):                Latitude of location   
        lon (float):                Longitude of location 
        verbose (bool, optional):   Print information. Defaults to False.

    Returns:
        int     Index of nearest grid point.
    """
    dist = [np.sqrt((lats[i]-lat)**2 + (lons[i]-lon)**2) for i in range(len(lats))]
    ind = np.where(dist==np.min(dist))[0][0]

    if verbose:
        print(f'Closest ind: {ind}')
        print(f' Given lat: {lat:.3f} vs found lat: {lats[ind]:.3f}')
        print(f' Given lat: {lon:.3f} vs found lon: {lons[ind]:.3f}')

    return ind

def deaverage(arr):
    '''
    de-average variables which contain the values which have been
    averaged since the beginning of the model simulation

    input:
    arr     1d array

    output:
    avg     1d array (1 element shorter than arr)
    '''
    x_ = np.zeros(len(arr) - 1)
    for i in range(1, len(arr)):   
        x_[i-1] = (arr[i]*(i) - arr[i-1]*(i-1))
    return x_


