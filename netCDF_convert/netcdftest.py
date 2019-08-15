# this file is just for me to see the properties of each of the netcdf variables

import netCDF4 as nc

ds1 = nc.Dataset('quasisymmetry_out.20190105-01-012_nfp1_stellSym.nc')

var = [ds1.variables['nfp'][:],  # 0
       ds1.variables['sign_G'][:],  # 1
       ds1.variables['sign_psi'][:],  # 2
       ds1.variables['resolution_option'][:],  # 3
       ds1.variables['sigma_initial_min'][:],  # 4
       ds1.variables['sigma_initial_max'][:],  # 5
       ds1.variables['sigma_initial_N_scan'][:],  # 6
       ds1.variables['sigma_initial_scan_option'][:],  # 7
       ds1.variables['eta_bar_min'][:],  # 8
       ds1.variables['eta_bar_max'][:],  # 9
       ds1.variables['eta_bar_N_scan'][:],  # 10
       ds1.variables['eta_bar_scan_option'][:],  # 11
       ds1.variables['Fourier_scan_option'][:],  # 12
       ds1.variables['max_precise_elongation'][:],  # 13
       ds1.variables['max_elongation_to_keep'][:],  # 14
       ds1.variables['max_max_curvature_to_keep'][:],  # 15
       ds1.variables['min_iota_to_keep'][:],  # 16
       ds1.variables['iotas'][:],  # 17 - Long 1-D array
       ds1.variables['max_elongations'][:],  # 18 - Long 1-D array
       ds1.variables['rms_curvatures'][:],  # 19 - Long 1-D array
       ds1.variables['max_curvatures'][:],  # 20 - Long 1-D array
       ds1.variables['axis_lengths'][:],  # 21 - Long 1-D array
       ds1.variables['standard_deviations_of_R'][:],  # 22 - Long 1-D array
       ds1.variables['standard_deviations_of_Z'][:],  # 23 - Long 1-D array
       ds1.variables['axis_helicities'][:],  # 24 - Long 1-D array
       ds1.variables['B_helicities'][:],  # 25 - Long 1-D array
       ds1.variables['effective_nfps'][:],  # 26 - Long 1-D array
       ds1.variables['Newton_tolerance_achieveds__logical__'][:],  # 27 - Long 1-D array
       ds1.variables['iota_tolerance_achieveds__logical__'][:],  # 28 - Long 1-D array
       ds1.variables['elongation_tolerance_achieveds__logical__'][:],  # 29 - Long 1-D array
       ds1.variables['R0s_min'][:],  # 30
       ds1.variables['R0s_max'][:],  # 31
       ds1.variables['R0s_N_scan'][:],  # 32
       ds1.variables['R0c_min'][:],  # 33
       ds1.variables['R0c_max'][:],  # 34
       ds1.variables['R0c_N_scan'][:],  # 35
       ds1.variables['Z0s_min'][:],  # 36
       ds1.variables['Z0s_max'][:],  # 37
       ds1.variables['Z0s_N_scan'][:],  # 38
       ds1.variables['Z0c_min'][:],  # 39
       ds1.variables['Z0c_max'][:],  # 40
       ds1.variables['Z0c_N_scan'][:],  # 41
       ds1.variables['scan_sigma_initial'][:],  # 42 - Long 1-D array
       ds1.variables['sigma_initial_values'][:],  # 43
       ds1.variables['scan_eta_bar'][:],  # 44 - Long 1-D array
       ds1.variables['eta_bar_values'][:],  # 45
       ds1.variables['N_scan_array'][:],  # 46
       ds1.variables['scan_R0c'][:],  # 47 - Long 2-D array: len=4
       ds1.variables['scan_R0s'][:],  # 48 - Long 2-D array: len=4
       ds1.variables['scan_Z0c'][:],  # 49 - Long 2-D array: len=4
       ds1.variables['scan_Z0s'][:]]  # 50 - Long 2-D array: len=4

count = 0
for n in var:
    print('=-=-=-=-=', count, '=-=-=-=-=')
    print(n[1])
    print()
    count += 1
