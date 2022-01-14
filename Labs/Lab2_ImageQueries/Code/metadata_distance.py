# -*- coding: utf-8 -*-
import math
import numpy as np
import scipy.cluster.hierarchy as h_cluster
from scipy.cluster.hierarchy import linkage as h_linkage
import scipy.spatial.distance as ssd
from geopy.distance import geodesic


def has_geotag(d):
    # geotag is at position 1, has zero value if geotag was not found included
    return d[1] != 0

def lonlat_to_decimal(geo):
    # example ([52, 0, 36], 'N', [4, 21, 36], 'E', 'delft')
    result = [geo[0][0] + geo[0][1] / 60.0 + geo[0][2]/3600.0, geo[2][0] + geo[2][1] / 60.0 + geo[2][2]/3600.0]    
    
    if geo[1] == 'S':
        result[0] = -result[0]
    if geo[3] == 'W':
        result[1] = -result[1]
        
    return (result[0], result[1])    
        
def compute_geographic_distance(m1,m2):
    geographical_dist = -1
    if not has_geotag(m1) or not has_geotag(m2):
        # can't do geographic distance
        geographical_dist = 0        
    else:
        geo1 = lonlat_to_decimal(m1[1])
        geo2 = lonlat_to_decimal(m2[1])
        
        geographical_dist = geodesic(geo1,geo2)
    return geographical_dist.meters



