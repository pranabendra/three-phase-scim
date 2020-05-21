#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..classes.metric import Length
from ..rotorDesign.airGapLength import getAirGapLength
from math import sqrt

def air_gap(L, D, air_gap_matrix):
    lg = Length(0)
    Dr = Length(0)
    
    lg.setLength(round(getAirGapLength(D.m, air_gap_matrix), 2) *pow(10, -3))
    print("Airgap: ", lg.mm)
    
    Dr.setLength(D.m - 2*lg.m)
    print("Diameter of rotor: ", Dr.mm)
    
    return lg, Dr
    