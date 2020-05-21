#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..classes.metric import Length,Area
from math import pi

def rotor_slot_leakage(Ws,W0,h1,h3,h4,Kws,Ss,Sr):
    sp_slot_per=4*pi*pow(10,-7)*(2*h1.m/(3*Ws.m)+2*h3.m/(Ws.m+W0.m)+h4.m/W0.m)
    print("Specific slot permeance for rotor:",sp_slot_per)
    
    slot_perm_stator=sp_slot_per*Kws*Kws*Ss/Sr
    print("Referred to stator side:",slot_perm_stator)
    
    return slot_perm_stator