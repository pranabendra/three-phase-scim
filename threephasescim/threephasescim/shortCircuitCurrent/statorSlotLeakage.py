#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi
from ..classes.metric import Length, Area

def stator_slot_leakage(Ws, W1, W0, isCircular, h1, h3, h4):
    print(W1.m, W0.m, Ws.m)
    if isCircular:
        sp_slot_per = 4*pi*pow(10,-7)*(2*h1.m/(3*(Ws.m + W1.m))+2*h3.m/(W1.m + W0.m) + h4.m/W0.m)
    else:
        sp_slot_per = 4*pi*pow(10,-7)*(2*h1.m/(3*Ws.m) + 2*h3.m/(Ws.m + W0.m)+ h4.m/W0.m)
    
    print("Specific slot permeance for stator: ", sp_slot_per)    
    return sp_slot_per
