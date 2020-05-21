#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..classes.metric import Length,Area
from ..noLoadCurrent.LohysLoss import getSpecificIronLoss
from math import pi

def loss_stator_core(D0, D, dss, Li, Bcs, lohys_loss_matrix):
    V_core = pi*(pow(D0.m,2) - pow((D.m+2*dss.m), 2))*Li.m/4
    print("Volume of stator core: ", V_core)
    
    weight_core = V_core*7.6*pow(10,3)
    print("Weight of stator core: ", weight_core)
    
    print("Flux density in core: ", Bcs)
    
    sploss = getSpecificIronLoss(Bcs, lohys_loss_matrix)
    print("Iron loss per kg: ", sploss)
    
    loss_core = sploss*weight_core
    print("Iron loss in core: ", loss_core)
    
    return loss_core
