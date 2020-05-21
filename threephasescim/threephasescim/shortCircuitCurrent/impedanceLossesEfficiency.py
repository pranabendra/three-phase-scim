#!/usr/bin/env python3
# -*- coding: utf-8 -*
from math import sqrt,pi,acos
from ..rating import line_voltage,power_in_kw

def Z_losses_eff(Rs,Xs,stator_copper,rotor_copper,no_load):
    Z=sqrt(pow(Rs,2)+pow(Xs,2))
    print("Total impedance of rotor at standstill:",Z)
    
    Isc=line_voltage/Z
    print("Isc:",Isc)
    
    pf_sc=Rs/Z
    print("short circuit power factor:",pf_sc)
    
    phase_sc=acos(pf_sc)*180/pi
    print("Phase angle of short circuit current:",phase_sc)
    
    loss_fl=stator_copper+rotor_copper+no_load
    print("Total loss at full load:",loss_fl)
    
    eff=100*power_in_kw*1000/(power_in_kw*1000+loss_fl)
    print("Efficiency:",eff)
    
    return Z,Isc,pf_sc,phase_sc,loss_fl,eff
