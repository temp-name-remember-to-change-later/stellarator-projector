# http://www.ceda.ac.uk/static/media/uploads/ncas-reading-2015/10_read_netcdf_python.pdf
# http://projector.tensorflow.org/

from time import time
import netCDF4 as nc
start = time()

# Change the value of this variable to 'csv' or 'tsv' depending on which format you want to use.
tsvcsv = 'tsv'
print('Reading file...', end=' ')

# Uncomment one at a time to extract individual files
ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-012_nfp1_stellSym.nc'); filename = 'data1.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-013_nfp2_stellSym.nc'); filename = 'data2.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-014_nfp3_stellSym.nc'); filename = 'data3.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-015_nfp4_stellSym.nc'); filename = 'data4.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-019_nfp5_stellSym.nc'); filename = 'data5.{}'.format(tsvcsv)

names = ['iotas', 'max_elongations', 'rms_curvatures' , 'max_curvatures', 'axis_lengths', 'standard_deviations_of_R',
          'standard_deviations_of_Z', 'axis_helicities', 'B_helicities', 'effective_nfps',
          'Newton_tolerance_achieveds__logical__', 'iota_tolerance_achieveds__logical__',
          'elongation_tolerance_achieveds__logical__', 'scan_sigma_initial', 'scan_eta_bar', 'scan_R0c[0]', 'scan_R0c[1]',
          'scan_R0c[2]', 'scan_R0c[3]', 'scan_R0s[0]', 'scan_R0s[1]', 'scan_R0s[2]', 'scan_R0s[3]', 'scan_Z0c[0]',
          'scan_Z0c[1]', 'scan_Z0c[2]', 'scan_Z0c[3]', 'scan_Z0s[0]', 'scan_Z0s[1]', 'scan_Z0s[2]', 'scan_Z0s[3]']

# This will all be fed into an unsupervised data classification thingy so labels aren't important (hopefully)
# Also this could be far more compact but I already typed it
var = [ds.variables['iotas'][:],  # 17 - Long 1-D array
       ds.variables['max_elongations'][:],  # 18 - Long 1-D array
       ds.variables['rms_curvatures'][:],  # 19 - Long 1-D array
       ds.variables['max_curvatures'][:],  # 20 - Long 1-D array
       ds.variables['axis_lengths'][:],  # 21 - Long 1-D array
       ds.variables['standard_deviations_of_R'][:],  # 22 - Long 1-D array
       ds.variables['standard_deviations_of_Z'][:],  # 23 - Long 1-D array
       ds.variables['axis_helicities'][:],  # 24 - Long 1-D array
       ds.variables['B_helicities'][:],  # 25 - Long 1-D array
       ds.variables['effective_nfps'][:],  # 26 - Long 1-D array
       ds.variables['Newton_tolerance_achieveds__logical__'][:],  # 27 - Long 1-D array
       ds.variables['iota_tolerance_achieveds__logical__'][:],  # 28 - Long 1-D array
       ds.variables['elongation_tolerance_achieveds__logical__'][:],  # 29 - Long 1-D array
       ds.variables['scan_sigma_initial'][:],  # 42 - Long 1-D array
       ds.variables['scan_eta_bar'][:],  # 44 - Long 1-D array
       ds.variables['scan_R0c'][:][0],  # 47 - Long 2-D array: len=4
       ds.variables['scan_R0c'][:][1],  # 47 - Long 2-D array: len=4
       ds.variables['scan_R0c'][:][2],  # 47 - Long 2-D array: len=4
       ds.variables['scan_R0c'][:][3],  # 47 - Long 2-D array: len=4
       ds.variables['scan_R0s'][:][0],  # 48 - Long 2-D array: len=4
       ds.variables['scan_R0s'][:][1],  # 48 - Long 2-D array: len=4
       ds.variables['scan_R0s'][:][2],  # 48 - Long 2-D array: len=4
       ds.variables['scan_R0s'][:][3],  # 48 - Long 2-D array: len=4
       ds.variables['scan_Z0c'][:][0],  # 49 - Long 2-D array: len=4
       ds.variables['scan_Z0c'][:][1],  # 49 - Long 2-D array: len=4
       ds.variables['scan_Z0c'][:][2],  # 49 - Long 2-D array: len=4
       ds.variables['scan_Z0c'][:][3],  # 49 - Long 2-D array: len=4
       ds.variables['scan_Z0s'][:][0],  # 50 - Long 2-D array: len=4
       ds.variables['scan_Z0s'][:][1],  # 50 - Long 2-D array: len=4
       ds.variables['scan_Z0s'][:][2],  # 50 - Long 2-D array: len=4
       ds.variables['scan_Z0s'][:][3]]  # 50 - Long 2-D array: len=4

file = open(filename, 'w')

# 'To add a row at the top of the file with the labels for all the data, uncomment these lines.'
#
# first = True
# for label in names:
#     if first:
#         first = False
#     else:
#         if tsvcsv == 'tsv':
#             file.write('\t')
#         elif tsvcsv == 'csv':
#             file.write(',')
#         else:
#             print('Error: Invalid file format (choose tsv or csv)')
#             exit(1)
#     file.write("'")
#     file.write(label)
#     file.write("'")

print(len(var[0]), 'lines read')
print('Writing items...')
percent = 0
inc = 20
for column in range(len(var[0])):
    if(column % (len(var[0]) // inc) == 0 and column != 0):
        percent += 100 / inc
        print(int(percent), '% done', sep='')
    firstchar = True
    for row in var:
        if firstchar:
            firstchar = False
        else:
            if tsvcsv == 'tsv':
                file.write('\t')
            elif tsvcsv == 'csv':
                file.write(',')
            else:
                print('Error: Invalid file format (choose tsv or csv)')
                exit(1)
        file.write(str(row[column]))
    file.write('\n')
file.close()

end = time()
print('\nDone')
print('Time elapsed (s): ', round(end - start, 2), 's', sep='')
