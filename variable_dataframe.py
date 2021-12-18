import pandas as pd

vdf = pd.DataFrame(
        # variables
        columns = ['lw_net', 'lw_down', 'lw_up', 'tqc', 'sw_net', 'latent_heat', 'sensible_heat',
                   'temp', 'qc', 'qv', 'qv_s', 'Ts', 'Ws', 'bs_latent_heat', 'pl_latent_heat', 'turb_coeff', 'v_10m', 'u_10m'],
        # attributes
        index = ['var_name', 'long_name', 'short_name',
                 'unit', 'min_value', 'max_value', 'var_id',
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
vdf['lw_net'].min_value   = -120
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
vdf['lw_down'].var_id      = '175'

vdf['lw_up'].var_name    = 'ATHU_S'
vdf['lw_up'].long_name   = 'Upward longwave radiation'
vdf['lw_up'].unit        = 'W m-2'
vdf['lw_up'].short_name  = 'lw_up'
vdf['lw_up'].min_value   = -100
vdf['lw_up'].max_value   = 10
vdf['lw_up'].color       = 'orange'
vdf['lw_up'].marker      = 'o'
vdf['lw_up'].avg         = True
vdf['lw_up'].mult        = (-1)
vdf['lw_up'].var_id      = '1531'

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
vdf['latent_heat'].avg         = True 

vdf['bs_latent_heat'].var_name    = 'ALHFL_BS'
vdf['bs_latent_heat'].long_name   = 'Bare soil latent heat'
vdf['bs_latent_heat'].unit        = 'W m-2'
vdf['bs_latent_heat'].short_name  = 'BS_LH'
vdf['bs_latent_heat'].min_value   = -200
vdf['bs_latent_heat'].max_value   = 50
vdf['bs_latent_heat'].color       = 'red'
vdf['bs_latent_heat'].marker      = 'o'
vdf['bs_latent_heat'].avg         = True 

vdf['pl_latent_heat'].var_name    = 'ALHFL_PL'
vdf['pl_latent_heat'].long_name   = 'Plant latent heat'
vdf['pl_latent_heat'].unit        = 'W m-2'
vdf['pl_latent_heat'].short_name  = 'PL_LH'
vdf['pl_latent_heat'].min_value   = -200
vdf['pl_latent_heat'].max_value   = 50
vdf['pl_latent_heat'].color       = 'blue'
vdf['pl_latent_heat'].marker      = 'o'
vdf['pl_latent_heat'].avg         = True 

vdf['sensible_heat'].var_name    = 'ASHFL_S'
vdf['sensible_heat'].long_name   = 'Net sensible heat'
vdf['sensible_heat'].unit        = 'W m-2'
vdf['sensible_heat'].short_name  = 'SH'
vdf['sensible_heat'].min_value   = -200
vdf['sensible_heat'].max_value   = 50
vdf['sensible_heat'].color       = 'yellow'
vdf['sensible_heat'].marker      = 'o'
vdf['sensible_heat'].avg         = True 
vdf['sensible_heat'].var_id      = '2786' #not sure...

vdf['tqc'].var_name    = 'TQC'
vdf['tqc'].long_name   = 'Liquid water path'
vdf['tqc'].unit        = 'kg m-2'
vdf['tqc'].short_name  = 'LWP'
vdf['tqc'].min_value   = 0
vdf['tqc'].max_value   = 0.05
vdf['tqc'].color       = 'green'
vdf['tqc'].marker      = 'o'
vdf['tqc'].var_id      = '5547'

vdf['Ts'].var_name    = 'T_G'
vdf['Ts'].long_name   = 'Temperature at the ground-atm interface'
vdf['Ts'].unit        = 'K'
vdf['Ts'].short_name  = 'Ts'
vdf['Ts'].min_value   = 270
vdf['Ts'].max_value   = 290
vdf['Ts'].color       = 'gray'
vdf['Ts'].marker      = 'o'
vdf['Ts'].var_id      = '201'

vdf['Ws'].var_name    = 'W_I'
vdf['Ws'].long_name   = 'Interception storage water'
vdf['Ws'].unit        = 'Kg m-2'
vdf['Ws'].short_name  = 'Ws'
vdf['Ws'].min_value   = 0
vdf['Ws'].max_value   = 0.25
vdf['Ws'].color       = 'black'
vdf['Ws'].marker      = 'o'
vdf['Ws'].mult        = 1
vdf['Ws'].avg         = False

vdf['qv'].var_name    = 'QV'
vdf['qv'].long_name   = 'Specific humidity'
vdf['qv'].unit        = 'g/Kg'
vdf['qv'].short_name  = 'qv'
vdf['qv'].min_value   = 3.5
vdf['qv'].max_value   = 5
vdf['qv'].color       = 'black'
vdf['qv'].marker      = 'o'
vdf['qv'].mult        = 1000
vdf['qv'].avg         = False

vdf['qv_s'].var_name    = 'QV_S'
vdf['qv_s'].long_name   = 'Ground specific humidity'
vdf['qv_s'].unit        = 'g/Kg'
vdf['qv_s'].short_name  = 'qv_s'
vdf['qv_s'].min_value   = 3.5
vdf['qv_s'].max_value   = 5
vdf['qv_s'].color       = 'black'
vdf['qv_s'].marker      = 'o'
vdf['qv_s'].mult        = 1000
vdf['qv_s'].avg         = False

vdf['temp'].var_name    = 'T'
vdf['temp'].long_name   = 'Temperature'
vdf['temp'].unit        = 'K'
vdf['temp'].short_name  = 'temp'
vdf['temp'].min_value   = 272
vdf['temp'].max_value   = 282
vdf['temp'].color       = 'black'
vdf['temp'].marker      = 'o'
vdf['temp'].mult        = 1
vdf['temp'].avg         = False

vdf['turb_coeff'].var_name    = 'TCH'
vdf['turb_coeff'].long_name   = 'Turbulent transfer coefficient for heat and moisture'
vdf['turb_coeff'].unit        = ''
vdf['turb_coeff'].short_name  = 'turb_coeff'
vdf['turb_coeff'].min_value   = 0
vdf['turb_coeff'].max_value   = 0.09
vdf['turb_coeff'].color       = 'black'
vdf['turb_coeff'].marker      = 'o'
vdf['turb_coeff'].mult        = 1
vdf['turb_coeff'].avg         = False

vdf['v_10m'].var_name    = 'V_10M'
vdf['v_10m'].long_name   = 'Meridional wind at 10m above ground'
vdf['v_10m'].unit        = 'm s-1'
vdf['v_10m'].short_name  = 'v_10m'
vdf['v_10m'].min_value   = 0
vdf['v_10m'].max_value   = 1.25
vdf['v_10m'].color       = 'black'
vdf['v_10m'].marker      = 'o'
vdf['v_10m'].mult        = 1
vdf['v_10m'].avg         = False

vdf['u_10m'].var_name    = 'U_10M'
vdf['u_10m'].long_name   = 'Eastward wind at 10m above ground'
vdf['u_10m'].unit        = 'm s-1'
vdf['u_10m'].short_name  = 'u_10m'
vdf['u_10m'].min_value   = 0
vdf['u_10m'].max_value   = 0.25
vdf['u_10m'].color       = 'black'
vdf['u_10m'].marker      = 'o'
vdf['u_10m'].mult        = 1
vdf['u_10m'].avg         = False