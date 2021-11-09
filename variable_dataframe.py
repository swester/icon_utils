import pandas as pd

vdf = pd.DataFrame(
        # variables
        columns = ['lw_net', 'lw_down', 'lw_up', 'tqc', 'sw_net',
                   'temp', 'qc', 'qv', ],
        # attributes
        index = ['var_name', 'long_name', 'short_name',
                 'unit', 'min_value', 'max_value', 
                 # line appearance
                 'marker', 'linestyle', 'color',
                 # value transformations
                 'average', 'mult', 'add']
)

# set default values for certain attributes
vdf.loc['marker'][:] = 'o'
vdf.loc['linestyle'] = 'solid'
vdf.loc['color'] = 'black'
vdf.loc['mult'][:] = 1
vdf.loc['add'][:] = 0
vdf.loc['average'][:] = False

# fill variable dataframe with specific values

vdf['lw_net'].var_name    = 'ATHB_S'
vdf['lw_net'].long_name   = 'Net longwave radiation'
vdf['lw_net'].unit        = 'W m-2'
vdf['lw_net'].short_name  = 'LW_net'
vdf['lw_net'].min_value   = -100
vdf['lw_net'].max_value   = 10
vdf['lw_net'].color       = 'goldenrod'
vdf['lw_net'].marker      = 'o'


vdf['sw_net'].var_name    = 'ASOB_S'
vdf['sw_net'].long_name   = 'Net shortwave radiation'
vdf['sw_net'].unit        = 'W m-2'
vdf['sw_net'].short_name  = 'SW_net'
vdf['sw_net'].min_value   = -10
vdf['sw_net'].max_value   = 270
vdf['sw_net'].color       = 'blueviolet'
vdf['sw_net'].marker      = 'o'


vdf['tqc'].var_name    = 'TQC'
vdf['tqc'].long_name   = 'Liquid water path'
vdf['tqc'].unit        = 'kg m-2'
vdf['tqc'].short_name  = 'LWP'
vdf['tqc'].min_value   = 0
vdf['tqc'].max_value   = 0.05
vdf['tqc'].color       = 'blue'
vdf['tqc'].marker      = 'o'