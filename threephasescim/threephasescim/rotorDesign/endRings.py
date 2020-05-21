#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..classes.metric import Length, Area
from ..rating import poles
from math import pi, ceil
from ..rating import power_in_kw


def end_rings_rotor(Sr, Ib, Dr, Dsr, rotor_bar_loss):
    Ae_init = Area(0)
    Ae = Area(0)
    de = Length(0)
    tc = Length(0)
    outer_dia = Length(0)
    inner_dia = Length(0)
    mean_dia = Length(0)
    
    Ie = Sr*Ib/(pi*poles)
    print("End ring current: ",Ie)
    
    current_density = 6 #A/mm2
    
    Ae_init.setArea((Ie/current_density)*pow(10, -6))
    print("Reqd end ring Area: ", Ae_init.mm2)
    
    Ae.setArea(round(ceil(Ae_init.mm2/10)*10)*pow(10, -6))# rounding off to nearest multiple of 10
    print("Final end ring area: ", Ae.mm2)

    delta_e = (current_density*Ae_init.mm2)/Ae.mm2
    print("Actual current density of end ring: ", delta_e)    

    de.setLength(0.01)# depth of end ring constant at 10 mm
    print("Depth of ring: ", de.mm)
    
    tc.setLength((Ae.mm2/10)*pow(10, -3))
    print("Thickness of ring: ",tc.mm)

    outer_dia.setLength(Dr.m - 2*Dsr.m)
    print("Outer diameter of end ring: ", outer_dia.mm)

    inner_dia.setLength(outer_dia.m - 2*de.m)
    print("Inner diameter of end rings: ", inner_dia.mm)        
    
    mean_dia.setLength((outer_dia.m + inner_dia.m)/2)
    print("Mean diameter of end ring: ", mean_dia.mm)
    
    res_ring = 0.021*pi*mean_dia.m/Ae.mm2
    print("Resistance of each ring: ", res_ring)
    
    ring_copper_loss = 2*Ie*Ie*res_ring
    print("Copper loss in 2 end rings: ", ring_copper_loss)
    
    rotor_copper_loss = rotor_bar_loss + ring_copper_loss
    print("Total rotor copper loss: ", rotor_copper_loss)
    
    r = rotor_copper_loss/(power_in_kw*pow(10,3))

    slip = r/(1+r)
    print("Full load slip: ", slip*100)
    
    return rotor_copper_loss, slip, Ae, delta_e, mean_dia, res_ring, Ie, ring_copper_loss

    
        
    