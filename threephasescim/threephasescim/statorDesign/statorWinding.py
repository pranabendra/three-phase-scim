#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import path
import os
# path.insert(1, os.path.dirname(os.getcwd()))
from ..classes.metric import Length
from ..rating import line_voltage, poles, frequency, phase
from math import pi, ceil, sin

def stator_design_winding(Bav, tau, L, D, Kw, qs):
    yss = Length(0)
    
    flux_per_pole = Bav*tau*L
    print('Flux per pole:', round(flux_per_pole, 3))
    
    Ts = ceil(line_voltage/(4.44*frequency*flux_per_pole*Kw))
    print('Stator turns per phase:', round(Ts, 3))

    Ss = phase*qs*poles
    print('Stator slots:', Ss)

    yss.setLength(pi*D/Ss)
    print('Stator slot pitch:', round(yss.m, 3))

    stator_conductors = 2*phase*Ts
    print('Stator conductors:', stator_conductors)
    
    Zss = ceil(stator_conductors/Ss)
    print('Stator conductors per slot:', Zss)
    
    Cs = Ss/poles
    print('Coil span:', Cs)
    
    if (Cs%2==0):
        Kp = 0.966    #Kp=cos(60/2)
        Cs=Cs-1
        print("New Cs:",Cs)
    else:
        Kp = 1
        
    rad1 = (pi*30)/180
    rad2 = (pi*30)/(180*qs)
    Kd = sin(rad1)/(qs*sin(rad2))    
    
    Kws = Kp*Kd
    print('stator winding Factor:', Kws)
    
    return flux_per_pole, Ts, int(Ss), yss, Zss, Kws, Cs, Kp, Kd
