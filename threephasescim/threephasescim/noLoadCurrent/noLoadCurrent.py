#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..rating import power_in_kw, line_voltage
from ..noLoadCurrent.frictionWindageLoss import getFrictionWindageLoss
from math import sqrt, acos, pi

def no_load_current(loss_st, loss_sc, Im, Is, fwloss_matrix):
    iron_loss = 2*(loss_st + loss_sc)
    print("Total iron loss: ", iron_loss)
    
    fw_loss_percent = getFrictionWindageLoss(power_in_kw, fwloss_matrix)
    fw_loss = fw_loss_percent*power_in_kw*pow(10, 3)/100
    print("F and W loss: ", fw_loss)
    
    no_load_loss = iron_loss + fw_loss
    print("Total no load losses: ", no_load_loss)
    
    Il = no_load_loss/(3*line_voltage)
    print("Loss component of no load current per phase Il: ", Il)
    
    I0 = sqrt(pow(Im,2) + pow(Il,2))
    print("No load current: ", I0)
    
    I0_percent_Is = I0*100/Is
    print("No load current as percentage of full load current: ", I0_percent_Is)
    
    if(I0_percent_Is > 50):
        currentCriterion = False
    else:
        currentCriterion = True
    
    no_load_pf = Il/I0
    print("No load power factor: ", no_load_pf)
    
    phase_angle = acos(no_load_pf)*180/pi
    print("Phase angle of no load current: ", phase_angle)
    print("Current Criterion: ", currentCriterion)
    return I0, phase_angle, currentCriterion, no_load_loss, fw_loss, iron_loss, Il, no_load_pf
