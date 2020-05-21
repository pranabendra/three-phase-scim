#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..classes.metric import Length, Area
from math import pi
from ..rating import power_factor, poles, power_in_kw
from ..rotorDesign.selectConductor import select_conductor

def rotor_slots(Ss, Kws, Ts, Is, Dr, rect_mat, flux_per_pole, Li, L):
    rotor_slot_pitch = Length(0)
    rotor_bar_area = Area(0)
    Wsr = Length(0)
    Dsr = Length(0)
    slot_pitch_bottom = Length(0)
    Wt = Length(0)
    Wt_13 = Length(0)
    At_13 = Area(0)
    Lb = Length(0)
    Ws = Length(0)
    W0 = Length(0)
    h1 = Length(0)
    h3 = Length(0)
    h4 = Length(0)
    
    if poles == 6:
        Sr = Ss - 3
    else:
        Sr = Ss - 7
    print("No. of rotor slots: ", Sr)
    
    rotor_slot_pitch.setLength(pi*Dr.m/Sr)
    print("Rotor slot pitch: ", rotor_slot_pitch.mm)
    
    Ib = (2*3*Kws*Ts*Is*power_factor)/Sr
    print("Rotor bar current: ",Ib)
    
    rotor_current_density = 6 #in A/mm2
    
    rotor_bar_area.setArea((Ib/rotor_current_density)*pow(10, -6))
    print("Rotor bar area: ", rotor_bar_area.mm2)
    old_rotor_bar_area = rotor_bar_area.mm2
    
    all_areas, all_dims = select_conductor(rotor_bar_area.mm2, rect_mat, 0)
    
    i = 0#variable to be used later for iterating 
    flag = 1
    n = len(all_areas)

    if n==0:
        all_areas = [249, 249]
        all_dims = [(10, 25), (25, 10)]
        n = 2
    
    while(flag==1 and i<n):
        
        rotor_bar_area.setArea(all_areas[i]*pow(10, -6))
        print("Rotor bar area from table: ", rotor_bar_area.mm2)
    
        a, b = all_dims[i]
        
        if(b>a):#set depth to the larger value
            if power_in_kw < 10:
                Wsr.setLength((a+0.3)*pow(10,-3))
                Dsr.setLength((b+2.3)*pow(10,-3))
            elif 10<=power_in_kw<=50:
                Wsr.setLength((a+1)*pow(10,-3))
                Dsr.setLength((b+3)*pow(10,-3))
            elif power_in_kw > 50:
                Wsr.setLength((a+2)*pow(10,-3))
                Dsr.setLength((b+4)*pow(10,-3))
        else:
            if power_in_kw < 10:
                Wsr.setLength((b+0.3)*pow(10,-3))
                Dsr.setLength((a+2.3)*pow(10,-3))
            elif 10<=power_in_kw<=50:
                Wsr.setLength((b+1)*pow(10,-3))
                Dsr.setLength((a+3)*pow(10,-3))
            elif power_in_kw > 50:
                Wsr.setLength((b+2)*pow(10,-3))
                Dsr.setLength((a+4)*pow(10,-3))
    

        slot_pitch_bottom.setLength(pi*(Dr.m - 2*Dsr.m)/Sr)
        print("Slot pitch at bottom of slots: ", slot_pitch_bottom.mm)
    
        Wt.setLength(slot_pitch_bottom.m - Wsr.m)
        print("Tooth width at root: ", Wt.mm)
    
        flux_density_root = flux_per_pole*poles/(Sr*Li.m*Wt.m)
        print("Flux density at root of teeth: ", flux_density_root)
    
        if(flux_density_root<0.9):# flux density should not be a very low value
            t = Wsr.m
            Wsr.setLength(Dsr.m)
            Dsr.setLength(t)
        
        Wt_13.setLength((pi*(Dr.m - 4*Dsr.m/3)/Sr) - Wsr.m)
        print("Width of tooth at 1/3 height from narrow end: ", Wt_13.mm)
        print("Dsr: ", Dsr.mm)
        At_13.setArea((Sr*Wt_13.m*Li.m)/poles)
        print("Area of teeth at 1/3rd from narrow end: ", At_13.mm2)
        
        flux_density_13 = flux_per_pole/At_13.m2
        print("Flux density of rotor teeth at 1/3 from narrow end: ", flux_density_13)
        
        if (flux_density_13 > 1.25):  #1.7/1.36=1.25(1.25 is later used for no load calculation)
            flag = 1
            i = i+1
        else:
            flag = 0
       
    if(i>=n):
        noAreaFound=True
    else:
        noAreaFound=False
    
    Lb.setLength(L.m + 2*0.015 + 0.01)
    print("Length of each rotor bar: ", Lb.mm)
    
    R_rotor_bar = 0.021*Lb.m/rotor_bar_area.mm2
    print("Resistance of each bar(ohm):", R_rotor_bar)
    
    copper_loss = Sr*Ib*Ib*R_rotor_bar
    print("Total copper loss in bars(W): ", copper_loss)
    
    if(power_in_kw<10):
        W0.setLength(0.0015)
        Ws.setLength(Wsr.m)
        h1.setLength(Dsr.m)
        h3.setLength(0.001)
        h4.setLength(0.001)
    elif(10<=power_in_kw<=50):
        W0.setLength(0.002)
        Ws.setLength(Wsr.m)
        h1.setLength(Dsr.m)
        h3.setLength(0.0015)
        h4.setLength(0.0005)
    else:
        W0.setLength(0.002)
        Ws.setLength(Wsr.m)
        h1.setLength(Dsr.m)
        h3.setLength(0.003)
        h4.setLength(0.001)
    
    delta_r = (rotor_current_density*old_rotor_bar_area)/rotor_bar_area.mm2
    return Sr, Ib, rotor_bar_area, Wsr, Dsr, flux_density_13, copper_loss, Lb, rotor_slot_pitch, W0, Ws, h1, h3, h4, noAreaFound, delta_r, R_rotor_bar, a, b
