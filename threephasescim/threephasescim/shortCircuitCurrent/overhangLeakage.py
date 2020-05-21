#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi
from ..rating import poles, frequency
from ..shortCircuitCurrent.interpolateLeakage import getOverhangLeakage

def overhang_leakage(yss,tau,Cs,stator_slots,Ts,qs,slot_leakage_matrix):
    pole_pitch = stator_slots/poles
    ratio = Cs/pole_pitch
    print("Ratio: ",ratio)
    
    Ks = getOverhangLeakage(ratio, slot_leakage_matrix)
    print("Ks: ",Ks)
    
    L_lambda = 4*pi*pow(10,-7)*Ks*tau.m*tau.m/(pi*yss.m)
    print("Product L_lamba: ", L_lambda)
    
    X0 = 8*pi*frequency*Ts*Ts*L_lambda/(poles*qs)
    print("Overhang Leakage reactance X0: ", X0)
    
    return X0
