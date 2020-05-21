#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..rating import poles

def mag_no_load(Kws, Ts, ATg, ATts, ATcs, ATcr, ATtr):
    AT60 = ATg + ATts + ATcs + ATcr + ATtr
    print("AT60: ", AT60)
    
    Im = (0.427*poles*AT60)/(Kws*Ts)
    print("No load magnetising current: ", Im)
    
    return Im, AT60
