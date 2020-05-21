#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..rating import poles

def stator_teeth_actual(flux_per_pole, Ss, Wts, Li):
    flux_density_actual = flux_per_pole*poles/(Ss*Wts.m*Li.m)
    return flux_density_actual
    #Wb/m^2