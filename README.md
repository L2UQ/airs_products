## airs_products

Scripts for downloading and processing public AIRS products

### Preliminaries

* Accessing publicly available AIRS products from the [GES DISC](https://disc.gsfc.nasa.gov/) requires registration for a free NASA Earthdata acocunt.
* Additional steps and general instructions for downloading/subsetting products can be found at the [data access page](https://disc.gsfc.nasa.gov/data-access)
* Additional Python libraries needed: pandas, netCDF4, datetime, numpy
    - For OPenDAP accessibility in particular, it works best to install packages within an Anaconda environment
* If OPenDAP access will be used, a .dodsrc should be set up as outlined in the [GES DISC ncdump protocols](https://disc.gsfc.nasa.gov/data-access#ncdump)

### AIRS V7 Products

The AIRS Version 7 Level 2 support product includes retrievals of several geophysical quantities, including vertical profiles of temperature, humidity, and clouds. There are two options for accessing and subsetting the data products illustrated here. The first method uses the OPenDAP protocol to access the data on the remote server and subset variables, with a local file output that is about 10% of the size of the original files. The second method uses wget to download the full data product files, and a Python script then operates on the local copies. The OPenDAP approach is somewhat time consuming and requires additional configuration but yields a smaller final data volume locally.

1. OPenDAP
    - Set up the .dodsrc file as noted above
    - Navigate to the top level directory and run the Python script to extract the variables of interest  

            python airs_l2_proc_magic_dap.py  
2. wget and offline processing: check the [general wget instructions](https://disc.gsfc.nasa.gov/data-access#mac_linux_wget) from GES DISC
    - Navigate to the `/data` directory and download a list of AIRS support products

            wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i MAGIC_Ascending_201308_V7_wget.txt  
    The products total about 350 MB in size.  
    - Navigate to the top level directory and run the Python script to extract the variables of interest  

            python airs_l2_proc_magic.py  

The scripts will produce a NetCDF file with a subset of variables for each granule. The above steps can be repeated for the additional collection of ascending or descending granules by using `data/MAGIC_Ascending_201308_V7_wget.txt` and by changing the line reading `data/MAGIC_Ascending_201308_V7.csv` in the Python script.

