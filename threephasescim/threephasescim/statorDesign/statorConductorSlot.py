#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas
from ..classes.metric import Area, Length
from math import ceil, floor, pi, sqrt, exp
from ..rating import line_voltage, power_factor, efficiency, power_in_kw
from ..statorDesign.selectConductor import select_conductor

def stator_conductor_size_and_slot(flux_per_pole, Ss, poles, D, L, Li, tau, delta, Zss, space_factor, rectangular_excel_file, round_excel_file):
    def factorize(n):
        gm = sqrt(n)
        if gm == floor(gm):
            return gm, gm
        else:
            gm = floor(gm)
            while gm > 0:
                if n%gm == 0:
                    break
                gm -= 1
            return max(gm, n//gm), min(gm, n//gm)

    As = Area(0)
    space_conductors = Area(0)
    slot_area =  Area(0)
    stator_teeth_minm = Length(0)
    stator_teeth_actual = Length(0)
    slot_width_inner_W2 = Length(0)
    slot_width_outer_Ws = Length(0)
    slot_height_h1 = Length(0)
    dss = Length(0)
    Lmts = Length(0)
    lip_h4 = Length(0)
    wedge_h3 = Length(0)
    slot_opening_W0 = Length(0)
    
    Is = (power_in_kw*pow(10, 3))/(3*line_voltage*efficiency*power_factor)
    print('Stator current per phase:', Is)
    
    #delta is in A/mm^2
    As.setArea((Is*pow(10, -6)/delta))
    print('Stator conductor required area:', As.mm2)
    
    i = 0 #variable to be used later for iterating over areas for rectangular conductor
    
    if (As.mm2 > 10.5):
        isCircular = False
        all_As, all_dim = select_conductor(As.mm2, rectangular_excel_file, isCircular)
        # print(all_As, all_dim)
        As.setArea(all_As[i]*pow(10,-6))
        a,b = all_dim[i]
        ### Change the output variables
    else:
        isCircular = True
        _, new_As, d = select_conductor(As.mm2, round_excel_file, isCircular) # swg, new_As, d
        As.setArea(new_As*pow(10, -6))
        ### Change the output variables
        
    delta_s = Is/As.mm2
    print('Area of conductor needed: ', As.mm2)
    print('Actual current density(A/mm2): ', delta_s)
    
    space_conductors.setArea(Zss*As.m2)
    print('Space for bare conductors(mm2): ', space_conductors.mm2)
    
    slot_area.setArea(space_conductors.m2/space_factor) #used only for tapered slot
    print('Area of each slot(mm2): ', slot_area.mm2)
    
    stator_teeth_minm.setLength((flux_per_pole*poles)/(1.7*Ss*Li.m))
    print('Minimum stator teeth width: ', stator_teeth_minm.mm)
    
    func = 2 + stator_teeth_minm.mm - 2*exp(-stator_teeth_minm.mm/2)

    stator_teeth_actual.setLength((ceil(func))*pow(10, -3))
    print('Actual minimum tooth width: ', stator_teeth_actual.mm)
    
    
    if isCircular:
        lip_h4.setLength(0.001)
        wedge_h3.setLength(0.003)
        lip_wedge = lip_h4.mm+wedge_h3.mm
        
        slot_opening_W0.setLength(0.002)
        
        slot_width_inner_W2.setLength(((pi*(D.mm + 2*lip_wedge))/Ss - stator_teeth_actual.mm)*pow(10, -3))
        print("Inner slot width: ", slot_width_inner_W2.mm)
        a = pi/Ss
        b = slot_width_inner_W2.mm
        c = -slot_area.mm2
        slot_height_h1.setLength(max((-sqrt(pow(b,2)-4*a*c)-b)/(2*a)*pow(10, -3), (sqrt(pow(b,2)-4*a*c)-b)/(2*a)*pow(10, -3)))
        print('Slot height: ', slot_height_h1.mm)
        
        slot_width_outer_Ws.setLength(slot_width_inner_W2.m + (2*pi*slot_height_h1.m)/Ss)
        
        dss.setLength(slot_height_h1.m + lip_wedge*pow(10,-3))
        
    else:
        lip_h4.setLength(0.001)
        wedge_h3.setLength(0.003)
        lip_wedge = lip_h4.mm+wedge_h3.mm
        slot_width_inner_W2.setLength(((pi*(D.mm + 2*lip_wedge))/Ss - stator_teeth_actual.mm)*pow(10, -3))
        slot_width_outer_Ws.setLength(slot_width_inner_W2.m)
        z1 = int(slot_width_inner_W2.mm/a)
        z2 = int(slot_width_inner_W2.mm/b)

        print('z1: ', z1)
        print('z2: ', z2)
        print('a: ', a)
        print('b: ', b)
        
        lip_h4.setLength(0.001)
        wedge_h3.setLength(0.003)
        lip_wedge_slack = lip_h4.mm + wedge_h3.mm + 2
        
        slot_opening_W0.setLength(0.003)
        
        if(Zss%z1 == 0 and Zss%z2 != 0):
            z = Zss/z1
            slot_height_h1.setLength(z*b*pow(10, -3))
            dss.setLength((z*b + lip_wedge_slack + 1.5)*pow(10, -3))
            print('Entered 1')
        elif(Zss%z2 == 0 and Zss%z1 != 0):
            z = Zss/z2
            slot_height_h1.setLength(z*a*pow(10,-3))
            dss.setLength((z*a + lip_wedge_slack + 1.5)*pow(10, -3))
            print('Entered 2')
        elif(Zss%z1 == 0 and Zss%z2 == 0):
            if z1>z2:
                z = Zss/z1
                slot_height_h1.setLength(z*b*pow(10,-3))
                dss.setLength((z*b + lip_wedge_slack + 1.5)*pow(10, -3))
                print('Entered 3')
            else:
                z = Zss/z2
                slot_height_h1.setLength(z*a*pow(10, -3))
                dss.setLength((z*a + lip_wedge_slack + 1.5)*pow(10, -3))
                print('Entered 4')
        else:
            f1, f2 = factorize(Zss)
            print(f1, f2)
            if f1 <= z1 and f2 <= z2:
                slot_height_h1.setLength(f2*b*pow(10,-3))
                dss.setLength((f2*b + lip_wedge_slack + 1.5)*pow(10, -3))
                print('Entered 5')
            elif f2 <= z1 and f1 <= z2:
                slot_height_h1.setLength(f1*b*pow(10,-3))
                dss.setLength((f1*b + lip_wedge_slack + 1.5)*pow(10, -3))
                print('Entered 6')
            else:
                print('Mayday...')
    print('Slot Dimensions: ')
    
    if isCircular:
        print('Slot Type: Tapered')
        print('Slot Width Inner(at AA): ', slot_width_inner_W2.mm)
        print('slot width Outer(at bottom): ', slot_width_outer_Ws.mm)
        print('Depth of slot(in mm): ', dss.mm)
    else:
        print('Slot Type: Parallel')
        print('Slot Width(at AA): ', slot_width_inner_W2.mm)
        print('Depth of slot(in mm): ', dss.mm)
    
    flux_density_stator_teeth = (flux_per_pole*poles)/(Ss*stator_teeth_actual.m*Li.m)
    print('Actual flux density in stator teeth: ', flux_density_stator_teeth)
    
    Lmts.setLength((2*L.m + 2.3*tau.m + 0.24))
    print('Length of mean turn: ', Lmts.m)
    
    if isCircular:
        a = d
        b = d
    return Is, slot_width_inner_W2, slot_width_outer_Ws, dss, stator_teeth_actual, Lmts, isCircular, lip_h4, wedge_h3, slot_height_h1, flux_density_stator_teeth, As, a, b, delta_s