import matplotlib
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# modified scatterplot to allow list of markers (taken from https://github.com/matplotlib/matplotlib/issues/11155)

def mscatter(x,y,ax=None, m=None, **kw):
    if not ax: ax=plt.gca()
    sc = ax.scatter(x,y,**kw)
    if (m is not None) and (len(m)==len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, matplotlib.markers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = matplotlib.markers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# get markers to denote GCM

def run_markers(da): return [gcm_markers[g] if "_" in g else "$"+g+"$" for g in da.run.str.replace("p1_.+","p1").values]

gcm_markers = {'HadUK-Grid'                   : '*',
               'ECMWF-ERAINT_r1i1p1'          : '*',
               'CNRM-CERFACS-CNRM-CM5_r1i1p1' : 'o',
               'ICHEC-EC-EARTH_r12i1p1'       : 'p',
               'ICHEC-EC-EARTH_r1i1p1'        : 'h',
               'ICHEC-EC-EARTH_r3i1p1'        : 'H',
               'IPSL-IPSL-CM5A-MR_r1i1p1'     : "s",
               'MOHC-HadGEM2-ES_r1i1p1'       : 'P',
               'MPI-M-MPI-ESM-LR_r1i1p1'      : '<',
               'MPI-M-MPI-ESM-LR_r2i1p1'      : '^',
               'MPI-M-MPI-ESM-LR_r3i1p1'      : '>',
               'NCC-NorESM1-M_r1i1p1'         : 'X',
               'ACCESS1-3_r1i1p1'             : 'o',
               'BCC-CSM1-1_r1i1p1'            : 'p',            
               'CanESM2_r1i1p1'               : 'h',
               'CCSM4_r1i1p1'                 : 'H',            
               'CESM1-BGC_r1i1p1'             : 's', 
               'CMCC-CM_r1i1p1'               : '>', 
               'GFDL-ESM2G_r1i1p1'            : 'd', 
               'MPI-ESM-MR_r1i1p1'            : '^',
               'MRI-CGCM3_r1i1p1'             : '<',
               'ERAINT_r1i1p1'                : '*',
               'CNRM-CM5_r1i1p1'              : 'o',
               'EC-EARTH_r12i1p1'             : 'p',
               'EC-EARTH_r1i1p1'              : 'h',
               'EC-EARTH_r3i1p1'              : 'H',
               'IPSL-CM5A-MR_r1i1p1'          : "s",
               'HadGEM2-ES_r1i1p1'            : 'P',
               'MPI-ESM-LR_r1i1p1'            : '^',
               'MPI-ESM-LR_r2i1p1'            : '<',
               'MPI-ESM-LR_r3i1p1'            : '>',
               'NorESM1-M_r1i1p1'             : 'X'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# get colours to denote RCM

def run_colours(da): return ["black" if len(r) == 2 else rcm_colours[r] for r in da.run.str.replace(".+p1_","").values]

rcm_colours = {'ALADIN63'          : 'mediumblue',
               'CCLM4-8-17'        : 'blueviolet',
               'COSMO-crCLIM-v1-1' : 'mediumvioletred',
               'HIRHAM5'           : 'red',
               'HadREM3-GA7-05'    : 'darkorange',
               'RACMO22E'          : 'gold',
               'RCA4'              : 'yellowgreen',
               'REMO2015'          : 'green',
               'RegCM4-6'          : 'darkturquoise',
               'WRF381P'           : 'dodgerblue'}

# add CMIP5-EC runs (white symbols) to the RCM colour dictionary
rcm_colours.update({gcm : "w" for gcm in ['CNRM-CM5_r1i1p1', 'IPSL-CM5A-MR_r1i1p1', 'MPI-ESM-LR_r1i1p1', 'MPI-ESM-LR_r2i1p1',
                                          'MPI-ESM-LR_r3i1p1', 'EC-EARTH_r1i1p1', 'EC-EARTH_r12i1p1', 'NorESM1-M_r1i1p1', 'HadGEM2-ES_r1i1p1']})

# add CMIP5-13 runs (grey symbols) to the RCM colour dictionary
rcm_colours.update({gcm : "grey" for gcm in ['BCC-CSM1-1_r1i1p1', 'MRI-CGCM3_r1i1p1', 'CanESM2_r1i1p1', 'CESM1-BGC_r1i1p1', 'ACCESS1-3_r1i1p1', 
                                             'GFDL-ESM2G_r1i1p1', 'CCSM4_r1i1p1', 'CMCC-CM_r1i1p1', 'MPI-ESM-MR_r1i1p1'] if not gcm in rcm_colours.keys()})