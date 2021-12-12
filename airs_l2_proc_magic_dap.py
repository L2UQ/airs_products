# Process AIRS Level 2 for a sequence of granules
# Here files are accessed remotely via OpenDAP

from netCDF4 import Dataset
import pandas
import numpy
import datetime
import airs_l2_support

# Granule choices
grfrm = pandas.read_csv("data/MAGIC_Descending_201308_V7_DAP.csv", \
                        dtype = {'Mode':'string', 'Year':int, 'Month':int, 'Day':int, 'Granule':int, \
                                 'RefLon':float, 'RefLat':float, 'MinDist':float, 'L2File':'string'}, \
                        encoding='utf-8-sig')
ngrn = grfrm.shape[0]
dtdir = 'data/'

# Dimensions
airs_dims = pandas.read_csv("config/AIRS_Output_Dims.csv", dtype = {'DimName':'string', 'DimLen':int},encoding='utf-8-sig')

# Coordinates
airs_coords = pandas.read_csv("config/AIRS_Coord_Vars.csv", dtype = {'VarName':'string', 'Dims':int, 'Type':'string', 'Units':'string'}, \
                              encoding='utf-8-sig')
print(airs_coords['Units'])

# Variable List
airs_vars = pandas.read_csv("config/AIRS_L2_Vars.csv", dtype = {'VarName':'string', 'Dims':int, 'Type':'string', 'VertDim':'string'}, \
                            encoding='utf-8-sig')

# Extract data and write output
for k in range(ngrn):
    l2src = grfrm['L2File'].values[k]
    print(l2src)
    l2out = '%s/AIRS_V7_L2_%s_%04d.%02d.%02d.%03d.nc' % (dtdir,grfrm['Mode'].values[k],grfrm['Year'].values[k], \
                                                      grfrm['Month'].values[k],grfrm['Day'].values[k], \
                                                      grfrm['Granule'].values[k])
    airs_l2_support.extract_airs_l2_supp(l2src, l2out, airs_vars, airs_dims, airs_coords)

