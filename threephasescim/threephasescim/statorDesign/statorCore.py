#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..classes.metric import Length,Area
from math import ceil

def stator_core(flux_per_pole, Li, D, dss):
    Acs = Area(0)
    dcs_init = Length(0)
    dcs = Length(0)
    stator_outer_D0 = Length(0)
             
    flux_core = flux_per_pole/2
    
    flux_density = 1.2 #assumption
    
    Acs.setArea(flux_core/flux_density)
    print("Area of stator core: ", Acs.m2)
    
    dcs_init.setLength(Acs.m2/Li.m)
    print("Depth of core: ", dcs_init.mm)
    
    dcs.setLength(ceil(dcs_init.mm)*pow(10, -3))
    
    flux_density_core_actual = (dcs_init.mm*1.2)/dcs.mm
    print("Flux density in stator core: ", flux_density_core_actual)
    
    stator_outer_D0.setLength(D.m + 2*dss.m + 2*dcs.m)
    print("Outer diameter of stator laminations: ", stator_outer_D0.mm)
    
    return Acs, dcs, stator_outer_D0, flux_density_core_actual
    