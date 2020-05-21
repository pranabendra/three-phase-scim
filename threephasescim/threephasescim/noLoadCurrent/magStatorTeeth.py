#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..noLoadCurrent.LohysBAt import getATFromLohys
from ..rating import poles
from ..classes.metric import Area

def mag_stator_teeth(Ss, Wts, Li, Bts, dss, lohys_bat_matrix):
    teeth_pole_area = Area(0)
    
    teeth_pole_area.setArea(Ss*Wts.m*Li.m/poles)
    print("Area of teeth per pole: ", teeth_pole_area.m2)
    
    print("Flux density in stator teeth(Wb/m^2): ", Bts)
    
    Bts60 = 1.36*Bts
    print("Bts60: ", Bts60)
    
    alpha = getATFromLohys(Bts60, lohys_bat_matrix)
    print("alphats60: ", alpha)
    
    ATs = alpha*dss.m
    print("Mmf required for stator teeth: ", ATs)
    
    return ATs
