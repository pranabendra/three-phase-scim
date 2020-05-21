#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..classes.metric import Length, Area
from math import pi
from ..noLoadCurrent.LohysLoss import getSpecificIronLoss

def loss_stator_teeth(Ss, Wts, Li, dss, Bts, lohys_loss_matrix):
    V_st = Ss*Wts.m*Li.m*dss.m
    print("Volume of stator teeth: ", V_st)
    
    weight_st = V_st*7.6*pow(10,3)
    print("Weight of stator teeth: ", weight_st)
    
    Bm = pi*Bts/2
    print("Maximum flux density on stator teeth: ", Bm)
    
    sploss = getSpecificIronLoss(Bm, lohys_loss_matrix)
    print("Specific Iron loss: ", sploss)
    
    loss_st = sploss*weight_st
    print("Iron loss in stator teeth: ", loss_st)
    
    return loss_st
    