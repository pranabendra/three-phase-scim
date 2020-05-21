#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..rating import line_voltage,poles

def total_leakage(Im,Ss,Sr,xs,X0):
    Xm=line_voltage/Im
    print("Magnetizing reactance Xm:",Xm)
    
    qs=Ss/(3*poles)
    qr=Sr/(3*poles)
    
    Xz=(5*Xm*(1/pow(qs,2)+1/pow(qr,2)))/(6*9)#ms=3
    print("Xz:",Xz)
    
    XS =xs+X0+Xz
    print("Total leakage reactance per phase referred to stator:",XS)
    
    return Xm, XS, Xz
    