#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi
from ..classes.metric import Length,Area
from ..rating import ns

def temperature_rise(iron_loss,Pc,L,Lmts,D,D0,temp):
    out_surface=Area(0)
    in_surface=Area(0)
    both_ends_surface=Area(0)
    
    slot_copper_loss=2*L.m*Pc/Lmts.m
    print("Copper loss in slot portion:",slot_copper_loss)
    
    total1=iron_loss+slot_copper_loss
    print("Total loss to be dissipated by stator surface:",total1)
    
    out_surface.setArea(pi*D0.m*L.m)
    print("Outside cylindrical surface of stator:",out_surface.m2)
    
    in_surface.setArea(pi*D.m*L.m)
    print("Inner cylindrical surface area of stator:",in_surface.m2)
    
    Va=pi*D.m*ns
    print("Peripheral speed:",Va)
    
    both_ends_surface.setArea(pi*(pow(D0.m,2)-pow(D.m,2))/2)
    print("Cooling surface area of both ends:",both_ends_surface.m2)
    
    Vair=0.1*Va
    print("Velocity of air at end surface:",Vair)
    
    C1=[0.025, 0.030, 0.035, 0.04]
    C2=[0.03, 0.04, 0.05]
    C3=[0.08, 0.1, 0.15, 0.2]
    
    i=0#variable for iteratine over colling coefficient
    flag=1
    
    while(flag==1):
        print("Iteration:",(i))
        
        loss_back_core=out_surface.m2/C1[i]
        print("Loss dissipated from back of core:",loss_back_core)
        
        cool_coeff_inside=C2[i]/(1+0.1*Va)
        print("Cooling coefficient:", cool_coeff_inside)
        
        loss_inside_stator=in_surface.m2/cool_coeff_inside
        print("Loss dissipated from inside surface of stator:",loss_inside_stator)
        
        cool_coeff_end=C3[i]/Vair
        print("Cooling Coefficient:",cool_coeff_end)
        
        loss_end=both_ends_surface.m2/cool_coeff_end
        print("Loss dissipated from end surface:",loss_end)
        
        total2=loss_back_core+loss_end+loss_inside_stator
        print("Total loss dissipated:",total2)
        
        theta=total1/total2
        print("Temperature rise:",theta)
        
        if(theta<temp):
            flag=0
        else:
            i = i+1
    return theta
        
        
        
        