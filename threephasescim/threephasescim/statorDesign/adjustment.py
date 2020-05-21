from ..rating import frequency, phase, line_voltage

def adjust_initial_values(Zss, Ss, qs, old_Bav, ac, tau, L, Kw):
    Zss = round(Zss/4)*4
    stator_conductors = Zss*Ss
    Ts = round(stator_conductors/(qs*phase))
    flux_per_pole = line_voltage/(4.44*Ts*frequency*Kw)
    new_Bav = flux_per_pole/(tau.m*L.m)
    ac = round((old_Bav*ac)/new_Bav)
    print("New Zss: ", Zss)
    print("New Ts: ", Ts)
    print("New flux per pole: ", flux_per_pole)
    print("New Bav: ", new_Bav)
    print("New ac: ", ac)

    return flux_per_pole, Ts, Ss, Zss, new_Bav, ac