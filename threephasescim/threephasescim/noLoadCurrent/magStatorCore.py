#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..classes.metric import Length,Area
from ..noLoadCurrent.LohysBAt import getATFromLohys
from math import pi
from ..rating import poles

def mag_stator_core(D, Li, dcs, dss, Bcs, lohys_bat_matrix):
    Acs = Area(0)
    lcs = Length(0)
    
    Acs.setArea(Li.m*dcs.m)
    print("Area of stator core: ", Acs.m2)
    
    print("Flux density in stator core: ", Bcs)
    
    lcs.setLength(pi*(D.m + 2*dss.m + 2*dcs.m)/(3*poles))
    print("Length of magnetic path through stator core: ", lcs.m)
    
    alpha = getATFromLohys(Bcs, lohys_bat_matrix)
    print("alphatcs: ", alpha)
    
    ATcs = alpha*lcs.m
    print("Mmf required for stator core: ", ATcs)
    
    return ATcs
