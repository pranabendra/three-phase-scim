# from sys import path
# path.insert(1, './classes')
from ..classes.metric import Length, Area
from ..rating import power_factor, power_in_kw, efficiency, ns, poles, duct_exceed_length, duct_width
from math import pi

def compute_main_dimension(Bav, ac, Kw, L_by_tau):
    tau = Length(0)
    D = Length(0)
    L = Length(0)
    Li = Length(0)
    duct = False

    C0 = 11*Kw*Bav*ac*pow(10, -3)
    print("C0: ", round(C0,3))

    Q = power_in_kw/(power_factor*efficiency)
    print("KVA input: ", round(Q,2))

    product_D2L = Q/(C0*ns)
    print("D2L Product: ", product_D2L)

    L_by_D = L_by_tau*pi/poles
    D.setLength(pow(product_D2L/L_by_D, 1/3))
    L.setLength(L_by_D*D.m)
    tau.setLength(L.m/L_by_tau) 

    if L.m > duct_exceed_length:
        Li.setLength(0.9*(L.m - duct_width))
        duct = True
    else:
        Li.setLength(0.9*L.m)
        duct = False

    print("L: ", round(L.m, 3))
    print("D: ", round(D.m, 3))
    print("Li: ", round(Li.m, 3))
    print("tau: ", round(tau.m, 3))
    if duct:
        print("One duct of 10mm is present")
    else:
        print("No duct present")

    print('Main Dimension Completed')
    return D, L, tau, Li, duct, C0, Q, product_D2L
