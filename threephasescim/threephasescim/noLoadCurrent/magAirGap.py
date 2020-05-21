#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..noLoadCurrent.CarterCoeff import getCarterCoeff
from ..classes.metric import Length, Area
from math import pi
from ..rating import poles

def mag_air_gap(s_W0, r_W0, lg, yss, ysr, isDuct, duct_width_given, L, D, n_ducts, Bav, carter_matrix):
    Ag = Area(0)
    lge = Length(0)
    duct_width = Length(duct_width_given)
    
    r1 = s_W0.m/lg.m
    print("Ratio for stator: ", r1)
    
    Kcs = getCarterCoeff('semiClosed', r1, carter_matrix)
    print("Carter's coefficient for stator slots: ", Kcs)
    
    Kgss = yss.mm/(yss.mm - Kcs*s_W0.mm)
    print("Gap contraction factor for stator slots: ", Kgss)
    
    r2 = r_W0.m/lg.m
    print("Ratio for rotor: ", r2)
    
    Kcr = getCarterCoeff('semiClosed', r2, carter_matrix)
    print("Carter's coefficient for rotor slots: ", Kcr)
    
    Kgsr = ysr.mm/(ysr.mm - Kcr*r_W0.mm)
    print("Gap contraction factor for rotor slots: ", Kgsr)
    
    Kgs = Kgss*Kgsr
    print("Kgs: ", Kgs)
    
    if isDuct:
        r3 = duct_width.m/lg.m
        print("Ratio for duct: ", r3)
        
        Kcd = getCarterCoeff('open', r3, carter_matrix)
        print("Carter's coefficient for ducts: ", Kcd)
        
        Kgd = L.mm/(L.mm - Kcd*n_ducts*duct_width.mm)
        print("Gap contraction factor for ducts: ", Kgd)
        
    else:
        Kgd = 1
        
    Kg = Kgs*Kgd
    print("Total gap contraction factor: ", Kg)
        
    Ag.setArea(pi*D.m*L.m/poles)
    print("Area of air gap: ", Ag.m2)
    
    Bg60 = 1.36*Bav
    print("Bg60: ", Bg60)
    
    lge.setLength(Kg*lg.m)
    print("Effective length of air gap: ", lge.mm)
    
    ATg = 800000*Bg60*lge.m
    print("Mmf required for air gap: ", ATg)
    
    return ATg