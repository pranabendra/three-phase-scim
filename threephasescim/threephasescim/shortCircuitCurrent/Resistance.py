#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..rating import power_factor

def resistance(Ts,As,Lmts,Is,rotor_copper_loss):
    rs=0.021*Ts*Lmts.m/As.mm2
    print("Resistance of stator winding per phase:",rs)
    
    stator_copper_loss=3*Is*Is*rs
    print("Total stator copper loss:",stator_copper_loss)
    print("Total rotor copper loss:",rotor_copper_loss)
    print("Rotor copper loss per phase:",rotor_copper_loss/3)
    
    Rr=rotor_copper_loss/(Is*Is*pow(power_factor,2))
    print("Rotor resistance referred to stator:",Rr)
    
    Rs=rs+Rr
    print("Total resistance referred to stator Rs:",Rs)
    
    return Rs, stator_copper_loss, rs, Rr