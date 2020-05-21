#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..classes.metric import Length

def rotor_core(Dr, dcs, dsr, Bcs):
    dcr = Length(0)
    Di = Length(0)
    
    dcr.setLength(dcs.m)#same as stator core
    print("Depth of rotor core(same as stator): ", dcr.mm)
    
    Bcr = Bcs
    print("Flux density in rotor core(same as stator): ",Bcr)
    
    Di.setLength(Dr.m - 2*dsr.m - 2*dcr.m)
    print("Inner diameter or rotor laminations: ", Di.mm)
    
    return dcr, Bcr, Di
