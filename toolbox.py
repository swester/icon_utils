import numpy as np
import datetime as dt
import sys
import matplotlib.path as mpath
import xarray as xr
import six
import psyplot.project as psy

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

def get_dim_names(ds_var, verbose):
    """Retrieve dimension names for specific variable in xarray dataframe.

    Names for time/level/index - dimensions are listed in
    possible_xxx_names. For a given dataset containing only
    1 variable the function deduces the dimension names.

    Args:
        ds_var (xarray df): dataframe for 1 variable
        verbose (bool): print details

    Returns:
        dim_time (str)
        dim_index (str)
        dim_level (str)

    """
    possible_time_names = [
        "time",
    ]
    possible_index_names = ["ncells", "cells_1", "cells"]
    possible_level_names = [
        "height",
        "height_1",
        "height_2",
        "height_3",
        "height_4",
        "level",
        "level_1",
        "z_1",
        "z_2",
        "z_3",
    ]

    dim_time = None
    dim_index = None
    dim_level = None

    # loop over dims given in dataset
    for dim_names in ds_var.dims:

        # check for time names
        for time_name in possible_time_names:
            if time_name in dim_names:
                dim_time = time_name

                if verbose:
                    print(f"Found dim_time: {dim_time}.")
                break

        # check for index names
        for index_name in possible_index_names:
            if index_name in dim_names:
                dim_index = index_name

                if verbose:
                    print(f"Found dim_index: {dim_index}.")
                break

        # check for level names
        for level_name in possible_level_names:
            if level_name in dim_names:
                dim_level = level_name

                if verbose:
                    print(f"Found dim_level: {dim_level}.")
                break

    return dim_time, dim_index, dim_level

def mittelland_mask(lats, lons):
    """Mask for Swiss Plateau.

    Args:
        lats (np.array): latitudes of grid points
        lons (np.array): longitudes of grid points

    Returns:
        np.array filled with booleans: grid points within plateau = True
    """

    # Define the polygon to average in...
    ll_corner = (46.79, 6.56)
    p1 = (47.16, 7.29)
    p2 = (47.76, 9.08)
    p3 = (47.44, 9.28)
    p4 = (47.04, 8.00)
    p5 = (46.71, 6.76)

    # create polygon
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, ll_corner),
        (Path.LINETO, p1),
        (Path.LINETO, p2),
        (Path.LINETO, p3),
        (Path.LINETO, p4),
        (Path.LINETO, p5),
        (Path.CLOSEPOLY, ll_corner),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)

    # store original shape
    shape = lats.shape

    # path.contains_points checks whether points are within polygon
    # however, this function can only handle vectors
    # -> ravel and unravel
    latlon = [[lat, lon] for lat, lon in zip(lats.ravel(), lons.ravel())]
    mask = np.reshape(path.contains_points(latlon), shape)

    return mask

def deaverage(arr):
    """De-average values in array.

    Values of some variables have been averaged
    since beginning of the model simulation.

    Args:
        arr (1d array): ICON output variable

    Returns:
        1d array: de-averaged output

    """
    # length of input
    n = len(arr)

    # fill with nan (first value will stay nan)
    de_arr = np.empty(n)
    de_arr[:] = np.nan

    # calculate de-averaged values
    for i in range(1, len(arr)):
        de_arr[i] = arr[i] * (i) - arr[i - 1] * (i - 1)

    return de_arr

def validtime_from_leadtime(date, leadtime, verbose=False):
    """Calculate validtime from leadtime.

    Args:
        date (str or datetime obj): start of simulation (YYmmddHH or YYYYmmddHH)
        leadtime (int):             leadtime in hours
        verbose (bool):             print details

    Returns:
        datetime object

    """
    if isinstance(date, dt.datetime):
        ini = date
    else:
        try:
            ini = dt.datetime.strptime(date, "%y%m%d%H")
        except ValueError:
            try:
                ini = dt.datetime.strptime(date, "%Y%m%d%H")
            except ValueError:
                print(f"! problem in validtime_from_leadtime in utils.py!")
                print(f"  -> {date} does not match any known format")
                sys.exit()

    validtime = ini + dt.timedelta(hours=leadtime)

    if verbose:
        print(f"{date} + {leadtime}h = {validtime.strftime('%y%m%d%H')}")

    return validtime

def add_grid_info1(file, grid):
    """Add grid information to icon dataset.

    Args:
        file (str): icon output file in netcdf
        grid (str): icon grid file in netcdf

    Returns:
        xr.dataset: merged dataset

    """
    ds = xr.open_dataset(file).squeeze()
    ds_grid = xr.open_dataset(grid)

    # check how index is called in specified files
    grid_ind_name = 'cell'
    icon_ind_name = 'cells'

    # combine
    merged = ds.rename_dims({icon_ind_name:grid_ind_name}
                        ).assign_coords(
                        clon=('cell', np.float32(ds_grid.coords['clon'].values))
                        ).assign_coords(
                        clat=('cell', np.float32(ds_grid.coords['clat'].values))
                        ).assign_coords(
                        #clat_bnds=(('cell','vertices'), np.float32(ds_grid.coords['clat_vertices'].values))
                        clat_bnds=(('cell','vertices'), np.float32(ds_grid['clat_vertices'].values))
                        ).assign_coords(
                        #clon_bnds=(('cell','vertices'), np.float32(ds_grid.coords['clon_vertices'].values))
                        clon_bnds=(('cell','vertices'), np.float32(ds_grid['clon_vertices'].values))
                        )
    
    merged.clon.attrs['standard_name']='longitude'
    merged.clon.attrs['long_name']='center longitude'
    merged.clon.attrs['units']='radian'
    merged.clon.attrs['bounds']='clon_bnds'
    merged.clat.attrs['standard_name']='latitude'
    merged.clat.attrs['long_name']='center latitude'
    merged.clat.attrs['units']='radian'
    merged.clat.attrs['bounds']='clat_bnds'

    return merged

def add_encoding(obj):
    obj.encoding['coordinates'] = 'clat clon'

def add_grid_info2(nc_file, grid_file, index_name_grid = 'cell', index_name_fcst = 'ncells'):
    """Add grid information to icon dataset.

    Adapt dim-names from grid and icon file accordingly.

    Args:
        nc_file (str): icon output file
        grid_file (str): icon grid file
    """

    grid_ds = psy.open_dataset(grid_file)
    icon_ds = psy.open_dataset(nc_file).squeeze()

    data = icon_ds.rename({index_name_fcst: index_name_grid}).merge(grid_ds)

    # clat clon encoding needs to be added for each variable
    for k, v in six.iteritems(data.data_vars):
        add_encoding(v)
    return data
