#stellarator-projector

This is a script to convert certain netCDF files holding stellarator configuration data to .tsv and .csv files

##Requirements

This script uses Python 3, as well as [`netCDF4-python`](https://unidata.github.io/netcdf4-python/netCDF4/index.html).

##Usage

To use the script, first `git checkout` this repository and download the specific netCDF files [here](https://umd.app.box.com/s/5102vf5ynh6o0fztph2jq6dt8alt795k).

After unpacking the files, move them to the `ncdata` folder, then run `netcdfconvert.py`. This will convert the first of five files. To convert the rest, find the following lines in the file:

```
ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-012_nfp1_stellSym.nc'); filename = 'data1.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-013_nfp2_stellSym.nc'); filename = 'data2.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-014_nfp3_stellSym.nc'); filename = 'data3.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-015_nfp4_stellSym.nc'); filename = 'data4.{}'.format(tsvcsv)
# ds = nc.Dataset('../ncdata/quasisymmetry_out.20190105-01-019_nfp5_stellSym.nc'); filename = 'data5.{}'.format(tsvcsv)
```

and uncomment them one at a time for each file.

While the script is running, it will prompt you to pick whether you want to convert it to .csv or .tsv, and will ask whether or not you want to add a row with the data labels. To use the output file with the online TensorBoard Embedding Projector, type "tsv" and "N" (minus quotes).

The script in the `projector` folder is unfinished; it's meant to be a local implementation of the TBP. In the meantime, there is an [online version](projector.tensorflow.org), though it runs into issues with very large files, and it also limits the number of data points to 10,000 for t-SNE and 5,000 for UMAP.
