import pandas as pd

vdf = pd.DataFrame(
        # variables
        columns = ['lw_net', 'lw_down', 'lw_up', 'tqc', 'sw_net', 'latent_heat', 'sensible_heat',
                   'temp', 'qc', 'qv', ],
        # attributes
        index = ['var_name', 'long_name', 'short_name',
                 'unit', 'min_value', 'max_value', 
                 # line appearance
                 'marker', 'linestyle', 'color',
                 # value transformations
                 'avg', 'mult', 'add']
)

# set default values for certain attributes
vdf.loc['marker'][:] = 'o'
vdf.loc['linestyle'] = 'solid'
vdf.loc['color'] = 'black'
vdf.loc['mult'][:] = 1
vdf.loc['add'][:] = 0
vdf.loc['avg'][:] = False

# fill variable dataframe with specific values

vdf['lw_net'].var_name    = 'ATHB_S'
vdf['lw_net'].long_name   = 'Net longwave radiation'
vdf['lw_net'].unit        = 'W m-2'
vdf['lw_net'].short_name  = 'LW_net'
vdf['lw_net'].min_value   = -100
vdf['lw_net'].max_value   = 10
vdf['lw_net'].color       = 'goldenrod'
vdf['lw_net'].marker      = 'o'
vdf['lw_net'].avg         = True 

vdf['lw_down'].var_name    = 'ATHD_S'
vdf['lw_down'].long_name   = 'Downward longwave radiation'
vdf['lw_down'].unit        = 'W m-2'
vdf['lw_down'].short_name  = 'lw_down'
vdf['lw_down'].min_value   = -100
vdf['lw_down'].max_value   = 10
vdf['lw_down'].color       = 'red'
vdf['lw_down'].marker      = 'o'
vdf['lw_down'].avg         = True

vdf['lw_up'].var_name    = 'ATHU_S'
vdf['lw_up'].long_name   = 'Upward longwave radiation'
vdf['lw_up'].unit        = 'W m-2'
vdf['lw_up'].short_name  = 'lw_up'
vdf['lw_up'].min_value   = -100
vdf['lw_up'].max_value   = 10
vdf['lw_up'].color       = 'orange'
vdf['lw_up'].marker      = 'o'
vdf['lw_up'].avg         = True

vdf['sw_net'].var_name    = 'ASOB_S'
vdf['sw_net'].long_name   = 'Net shortwave radiation'
vdf['sw_net'].unit        = 'W m-2'
vdf['sw_net'].short_name  = 'SW_net'
vdf['sw_net'].min_value   = -10
vdf['sw_net'].max_value   = 270
vdf['sw_net'].color       = 'blue'
vdf['sw_net'].marker      = 'o'
vdf['sw_net'].avg         = True

vdf['latent_heat'].var_name    = 'ALHFL_S'
vdf['latent_heat'].long_name   = 'Net latent heat'
vdf['latent_heat'].unit        = 'W m-2'
vdf['latent_heat'].short_name  = 'LH'
vdf['latent_heat'].min_value   = -200
vdf['latent_heat'].max_value   = 50
vdf['latent_heat'].color       = 'pink'
vdf['latent_heat'].marker      = 'o'
vdf['latent_heat'].mult        = 1
vdf['latent_heat'].avg         = True 

vdf['sensible_heat'].var_name    = 'ASHFL_S'
vdf['sensible_heat'].long_name   = 'Net sensible heat'
vdf['sensible_heat'].unit        = 'W m-2'
vdf['sensible_heat'].short_name  = 'SH'
vdf['sensible_heat'].min_value   = -200
vdf['sensible_heat'].max_value   = 50
vdf['sensible_heat'].color       = 'yellow'
vdf['sensible_heat'].marker      = 'o'
vdf['sensible_heat'].mult        = 1
vdf['sensible_heat'].avg         = True 


vdf['tqc'].var_name    = 'TQC'
vdf['tqc'].long_name   = 'Liquid water path'
vdf['tqc'].unit        = 'kg m-2'
vdf['tqc'].short_name  = 'LWP'
vdf['tqc'].min_value   = 0
vdf['tqc'].max_value   = 0.05
vdf['tqc'].color       = 'darkblue'
vdf['tqc'].marker      = 'o'