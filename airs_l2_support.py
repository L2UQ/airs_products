# AIRS Level 2 supporting functions

from netCDF4 import Dataset
import numpy
import numpy.ma as ma
import datetime
import os
import pandas

def extract_airs_l2_supp(src_file, out_file, var_frm, dim_frm, coord_frm):
    '''Extract selected variables, dimensions, and coordinates from an AIRS
       Level 2 data file (granule) and produce an output file with
       selected variables extracted
    '''

    # Create output file
    l2out = Dataset(out_file,'w')

    ndim = dim_frm.shape[0]
    for i in range(ndim):
        dimtmp = l2out.createDimension(dim_frm['DimName'].values[i],dim_frm['DimLen'].values[i])
    l2out.close()

    # Coordinate variables
    ncrd = coord_frm.shape[0]
    for i in range(ncrd):
        cdim = coord_frm['Dims'].values[i]
        cvrnm = coord_frm['VarName'].values[i]
        cvrtp = coord_frm['Type'].values[i]
        cvunit = str(coord_frm['Units'].values[i])
        #print(cvrnm)
        if cvrtp == 'float':
            nctyp = 'f4'
            flvl = -9999
        elif cvrtp == 'double':
            nctyp = 'f8'
            flvl = -9999
        elif cvrtp == 'int':
            nctyp = 'i4'
            flvl = -99

        if cdim == 1:
            nccrd = Dataset('config/AIRSPressureLevels_Support.nc')
            tmpcrd = nccrd.variables[cvrnm][:]
            nccrd.close()
            l2out = Dataset(out_file,'r+')
            l2vr = l2out.createVariable(cvrnm,nctyp,[cvrnm], fill_value=flvl)
            l2vr[:] = tmpcrd
            if cvunit != '':
                l2vr.units = cvunit
            l2vr.missing_value = flvl
            l2out.close()
        elif cdim == 2:
            ncl2 = Dataset(src_file,'r')
            tmpcrd = ncl2.variables[cvrnm][:,:]
            ncl2.close()
            l2out = Dataset(out_file,'r+')
            l2vr = l2out.createVariable(cvrnm,nctyp,['GeoTrack','GeoXTrack'], fill_value=flvl)
            l2vr[:] = tmpcrd
            if cvunit != '':
                l2vr.units = cvunit
            l2vr.missing_value = flvl
            l2out.close()
        elif cdim == 4:
            ncl2 = Dataset(src_file,'r')
            tmpcrd = ncl2.variables[cvrnm][:,:,:,:]
            ncl2.close()
            l2out = Dataset(out_file,'r+')
            l2vr = l2out.createVariable(cvrnm,nctyp,['GeoTrack','GeoXTrack','AIRSTrack','AIRSXTrack'], fill_value=flvl)
            l2vr[:] = tmpcrd
            if cvunit != '':
                l2vr.units = cvunit
            l2vr.missing_value = flvl
            l2out.close()

    # Observed variables
    nvar = var_frm.shape[0]
    for i in range(nvar):
        vdim = var_frm['Dims'].values[i]
        vrnm = var_frm['VarName'].values[i]
        vrtp = var_frm['Type'].values[i]
        vvrt = str(var_frm['VertDim'].values[i])
        #print(cvrnm)
        if vrtp == 'float':
            nctyp = 'f4'
            flvl = -9999
        elif vrtp == 'double':
            nctyp = 'f8'
            flvl = -9999
        elif vrtp == 'int':
            nctyp = 'i4'
            flvl = -99

        if vdim == 2:
            ncl2 = Dataset(src_file,'r')
            tmpcrd = ncl2.variables[vrnm][:,:]
            ncl2.close()
            l2out = Dataset(out_file,'r+')
            l2vr = l2out.createVariable(vrnm,nctyp,['GeoTrack','GeoXTrack'], fill_value=flvl)
            l2vr[:] = tmpcrd
            l2vr.missing_value = flvl
            l2out.close()
        elif vdim == 3:
            ncl2 = Dataset(src_file,'r')
            tmpcrd = ncl2.variables[vrnm][:,:,:]
            ncl2.close()
            l2out = Dataset(out_file,'r+')
            l2vr = l2out.createVariable(vrnm,nctyp,['GeoTrack','GeoXTrack',vvrt], fill_value=flvl)
            l2vr[:] = tmpcrd
            l2vr.missing_value = flvl
            l2out.close()
        elif vdim == 4:
            ncl2 = Dataset(src_file,'r')
            tmpcrd = ncl2.variables[vrnm][:,:,:,:]
            ncl2.close()
            l2out = Dataset(out_file,'r+')
            l2vr = l2out.createVariable(vrnm,nctyp,['GeoTrack','GeoXTrack','AIRSTrack','AIRSXTrack'], fill_value=flvl)
            l2vr[:] = tmpcrd
            l2vr.missing_value = flvl
            l2out.close()
        elif vdim == 5:
            ncl2 = Dataset(src_file,'r')
            tmpcrd = ncl2.variables[vrnm][:,:,:]
            ncl2.close()
            l2out = Dataset(out_file,'r+')
            l2vr = l2out.createVariable(vrnm,nctyp,['GeoTrack','GeoXTrack','AIRSTrack','AIRSXTrack','Cloud'], fill_value=flvl)
            l2vr[:] = tmpcrd
            l2vr.missing_value = flvl
            l2out.close()

    return

def extract_airs_l1b(src_file, out_file, var_frm, dim_frm, coord_frm, chan):
    '''Extract selected variables, dimensions, and coordinates from an AIRS
       Level 1B data file (granule) and produce an output file with
       selected variables extracted
    '''

    # Create output file
    l1bout = Dataset(out_file,'w')

    ndim = dim_frm.shape[0]
    for i in range(ndim):
        dimtmp = l1bout.createDimension(dim_frm['DimName'].values[i],dim_frm['DimLen'].values[i])
    l1bout.close()

    # Coordinate variables
    ncrd = coord_frm.shape[0]
    for i in range(ncrd):
        cdim = coord_frm['Dims'].values[i]
        cvrnm = coord_frm['VarName'].values[i]
        cvrtp = coord_frm['Type'].values[i]
        cvunit = str(coord_frm['Units'].values[i])
        #print(cvrnm)
        if cvrtp == 'float':
            nctyp = 'f4'
            flvl = -9999
        elif cvrtp == 'double':
            nctyp = 'f8'
            flvl = -9999
        elif cvrtp == 'int':
            nctyp = 'i4'
            flvl = -99

        if cdim == 1:
            nccrd = Dataset('config/AIRSPressureLevels_Support.nc')
            tmpcrd = nccrd.variables[cvrnm][:]
            nccrd.close()
            l1bout = Dataset(out_file,'r+')
            l1bvr = l1bout.createVariable(cvrnm,nctyp,[cvrnm], fill_value=flvl)
            l1bvr[:] = tmpcrd
            if cvunit != '':
                l1bvr.units = cvunit
            l1bvr.missing_value = flvl
            l1bout.close()
        elif cdim == 2:
            ncl1b = Dataset(src_file,'r')
            tmpcrd = ncl1b.variables[cvrnm][:,:]
            ncl1b.close()
            l1bout = Dataset(out_file,'r+')
            l1bvr = l1bout.createVariable(cvrnm,nctyp,['L1BTrack','L1BXTrack'], fill_value=flvl)
            l1bvr[:] = tmpcrd
            if cvunit != '':
                l1bvr.units = cvunit
            l1bvr.missing_value = flvl
            l1bout.close()

    # Channels
    nctyp = 'f8'
    flvl = -9999
    l1bout = Dataset(out_file,'r+')
    l1bvr = l1bout.createVariable('Channel',nctyp,['Channel'], fill_value=flvl)
    l1bvr[:] = chan
    l1bvr.units = 'cm^-1'
    l1bvr.missing_value = flvl
    l1bout.close()

    # Observed variables
    nvar = var_frm.shape[0]
    for i in range(nvar):
        vdim = var_frm['Dims'].values[i]
        vrnm = var_frm['VarName'].values[i].decode('utf-8')
        vrtp = var_frm['Type'].values[i].decode('utf-8')
        #vvrt = str(var_frm['VertDim'].values[i])
        #print(cvrnm)
        if vrtp == 'float':
            nctyp = 'f4'
            flvl = -9999
        elif vrtp == 'double':
            nctyp = 'f8'
            flvl = -9999
        elif vrtp == 'int':
            nctyp = 'i4'
            flvl = -99

        if vdim == 2:
            ncl1b = Dataset(src_file,'r')
            tmpcrd = ncl1b.variables[vrnm][:,:]
            ncl1b.close()
            l1bout = Dataset(out_file,'r+')
            l1bvr = l1bout.createVariable(vrnm,nctyp,['L1BTrack','L1BXTrack'], fill_value=flvl)
            l1bvr[:] = tmpcrd
            l1bvr.missing_value = flvl
            l1bout.close()
        elif vdim == 3:
            ncl1b = Dataset(src_file,'r')
            tmpcrd = ncl1b.variables[vrnm][:,:,:]
            ncl1b.close()
            l1bout = Dataset(out_file,'r+')
            l1bvr = l1bout.createVariable(vrnm,nctyp,['L1BTrack','L1BXTrack','Channel'], fill_value=flvl)
            l1bvr[:] = tmpcrd
            l1bvr.missing_value = flvl
            l1bout.close()

    return

def extract_airs_ccr(src_file, out_file, var_frm, dim_frm, coord_frm, chan):
    '''Extract selected variables, dimensions, and coordinates from an AIRS
       cloud-cleared radiance data file (granule) and produce an output file with
       selected variables extracted
    '''

    # Create output file
    ccrout = Dataset(out_file,'w')

    ndim = dim_frm.shape[0]
    for i in range(ndim):
        dimtmp = ccrout.createDimension(dim_frm['DimName'].values[i],dim_frm['DimLen'].values[i])
    ccrout.close()

    # Coordinate variables
    ncrd = coord_frm.shape[0]
    for i in range(ncrd):
        cdim = coord_frm['Dims'].values[i]
        cvrnm = coord_frm['VarName'].values[i]
        cvrtp = coord_frm['Type'].values[i]
        cvunit = str(coord_frm['Units'].values[i])
        #print(cvrnm)
        if cvrtp == 'float':
            nctyp = 'f4'
            flvl = -9999
        elif cvrtp == 'double':
            nctyp = 'f8'
            flvl = -9999
        elif cvrtp == 'int':
            nctyp = 'i4'
            flvl = -99

        if cdim == 1:
            nccrd = Dataset('config/AIRSPressureLevels_Support.nc')
            tmpcrd = nccrd.variables[cvrnm][:]
            nccrd.close()
            ccrout = Dataset(out_file,'r+')
            ccrvr = ccrout.createVariable(cvrnm,nctyp,[cvrnm], fill_value=flvl)
            ccrvr[:] = tmpcrd
            if cvunit != '':
                ccrvr.units = cvunit
            ccrvr.missing_value = flvl
            ccrout.close()
        elif cdim == 2:
            ncccr = Dataset(src_file,'r')
            tmpcrd = ncccr.variables[cvrnm][:,:]
            ncccr.close()
            ccrout = Dataset(out_file,'r+')
            ccrvr = ccrout.createVariable(cvrnm,nctyp,['GeoTrack','GeoXTrack'], fill_value=flvl)
            ccrvr[:] = tmpcrd
            if cvunit != '':
                ccrvr.units = cvunit
            ccrvr.missing_value = flvl
            ccrout.close()

    # Channels
    nctyp = 'f8'
    flvl = -9999
    ccrout = Dataset(out_file,'r+')
    ccrvr = ccrout.createVariable('Channel',nctyp,['Channel'], fill_value=flvl)
    ccrvr[:] = chan
    ccrvr.units = 'cm^-1'
    ccrvr.missing_value = flvl
    ccrout.close()

    # Observed variables
    nvar = var_frm.shape[0]
    for i in range(nvar):
        vdim = var_frm['Dims'].values[i]
        vrnm = var_frm['VarName'].values[i].decode('utf-8')
        vrtp = var_frm['Type'].values[i].decode('utf-8')
        #vvrt = str(var_frm['VertDim'].values[i])
        #print(cvrnm)
        if vrtp == 'float':
            nctyp = 'f4'
            flvl = -9999
        elif vrtp == 'double':
            nctyp = 'f8'
            flvl = -9999
        elif vrtp == 'int':
            nctyp = 'i4'
            flvl = -99

        if vdim == 2:
            ncccr = Dataset(src_file,'r')
            tmpcrd = ncccr.variables[vrnm][:,:]
            ncccr.close()
            ccrout = Dataset(out_file,'r+')
            ccrvr = ccrout.createVariable(vrnm,nctyp,['GeoTrack','GeoXTrack'], fill_value=flvl)
            ccrvr[:] = tmpcrd
            ccrvr.missing_value = flvl
            ccrout.close()
        elif vdim == 3:
            ncccr = Dataset(src_file,'r')
            tmpcrd = ncccr.variables[vrnm][:,:,:]
            ncccr.close()
            ccrout = Dataset(out_file,'r+')
            ccrvr = ccrout.createVariable(vrnm,nctyp,['GeoTrack','GeoXTrack','Channel'], fill_value=flvl)
            ccrvr[:] = tmpcrd
            ccrvr.missing_value = flvl
            ccrout.close()

    return
