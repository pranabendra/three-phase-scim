#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi
from ..rating import frequency,poles
from ..classes.metric import Length

def slot_leakage_reactance(stator_perm,rotor_perm,Ts,L,qs):
    total_slot_perm=stator_perm+rotor_perm
    print("Total specific slot permeance:",total_slot_perm)
    
    xs=8*pi*frequency*Ts*Ts*total_slot_perm/(poles*qs)
    print("Slot leakage reactance xs(ohm):",xs)
    
    return xs