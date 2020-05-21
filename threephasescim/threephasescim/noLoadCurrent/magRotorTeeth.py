#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..noLoadCurrent.LohysBAt import getATFromLohys

def mag_rotor_teeth(Btr_13, dsr, lohys_bat_matrix):
    Btr60 = 1.36*Btr_13
    print("Btr60: ", Btr60)
    
    alpha = getATFromLohys(Btr60, lohys_bat_matrix)
    print("alpha_tr: ", alpha)
    
    ATr = alpha*dsr.m
    print("Mmf required for rotor teeth: ", ATr)
    
    return ATr
