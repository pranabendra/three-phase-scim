#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..classes.metric import Length,Area
from ..noLoadCurrent.LohysBAt import getATFromLohys
from ..rating import poles 
from math import pi

def mag_rotor_core(Bcr, Li, Dr, dsr, dcs, dcr, lohys_bat_matrix):
    Acr = Area(0)
    lcr = Length(0)
    
    Acr.setArea(Li.m*dcr.m)
    print("Area of rotor core: ", Acr.m2)
    
    print("Flux density in rotor core: ", Bcr)
    
    alpha = getATFromLohys(Bcr, lohys_bat_matrix)
    print("alpha_tsr: ", alpha)
    
    lcr.setLength(pi*(Dr.m - 2*dsr.m - dcs.m)/(3*poles))
    print("Length of flux path in rotor core: ", lcr.m)
    
    ATcr = alpha*lcr.m
    print("Mmf required for rotor core: ", ATcr)
    
    return ATcr
