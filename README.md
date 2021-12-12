## airs_product

Scripts for downloading and processing public AIRS products

### Preliminaries

* Accessing publicly available AIRS products from the [GES DISC](https://disc.gsfc.nasa.gov/) requires registration for a free NASA Earthdata acocunt.
* Additional steps and general instructions for downloading/subsetting products can be found at the [data access page](https://disc.gsfc.nasa.gov/data-access)
* Additional Python libraries needed

### AIRS V7 Products

1. OpenDAP
2. wget and offline processing: check the [general wget instructions](https://disc.gsfc.nasa.gov/data-access#mac_linux_wget) from GES DISC
    - Navigate to the `airs_products/data` directory and download a list of AIRS support products  
```
wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i MAGIC_Ascending_201308_V7_wget.txt
```
The products total about 350 MB in size.
    - Navigate to the `airs_products` directory and run the Python script to extract the variables of interest
```
python airs_l2_proc_magic.py
```
The script will produce a NetCDF file with a subset of variables for each of the downloaded products. The above steps can be repeated for the descending granules by using `MAGIC_Ascending_201308_V7_wget.txt` and by changing the line reading `MAGIC_Ascending_201308_V7.csv` in the Python script.
