from . import rating
from . import loadTable
import numpy
import pandas
import importlib
from .classes.metric import Length, Area
from .mainDimensions.mainDimensions import compute_main_dimension
from .statorDesign.statorWinding import stator_design_winding
from .statorDesign.adjustment import adjust_initial_values
from .statorDesign.statorConductorSlot import stator_conductor_size_and_slot
from .statorDesign.statorCore import stator_core
from .rotorDesign.airGap import air_gap
from .rotorDesign.rotorSlot import rotor_slots
from .rotorDesign.endRings import end_rings_rotor
from .rotorDesign.rotorCore import rotor_core
from .noLoadCurrent.magAirGap import mag_air_gap
from .noLoadCurrent.magStatorTeeth import mag_stator_teeth
from .noLoadCurrent.magStatorCore import mag_stator_core
from .noLoadCurrent.magRotorTeeth import mag_rotor_teeth
from .noLoadCurrent.magRotorCore import mag_rotor_core
from .noLoadCurrent.magNoLoad import mag_no_load
from .noLoadCurrent.lossStatorTeeth import loss_stator_teeth
from .noLoadCurrent.lossStatorCore import loss_stator_core
from .noLoadCurrent.noLoadCurrent import no_load_current
from .shortCircuitCurrent.statorSlotLeakage import stator_slot_leakage
from .shortCircuitCurrent.rotorSlotLeakage import rotor_slot_leakage
from .shortCircuitCurrent.slotLeakageReactance import slot_leakage_reactance
from .shortCircuitCurrent.overhangLeakage import overhang_leakage
from .shortCircuitCurrent.totalLeakage import total_leakage
from .shortCircuitCurrent.Resistance import resistance
from .shortCircuitCurrent.impedanceLossesEfficiency import Z_losses_eff
from .temperatureRise.temperatureRise import temperature_rise

def design_your_machine():
    swg_matrix, rect_matrix, carter_matrix, lohys_bat_matrix, fwloss_matrix, lohys_loss_matrix, air_gap_matrix, slot_leakage_matrix = loadTable.load_table()
    print()
    print()
    print('Hello!')
    print()
    print()

    # Variables
    Bav = 0.42
    Kw = 0.955
    ac = 20000
    qs = 2
    L_by_tau = 1.6
    delta = 6
    space_factor = 0.4

    count = 0
    currentCriterion = False
    while 1 - (currentCriterion  == True and Bav >= 0.35):
        Bav = 0.42
        # Enter Bav, ac, Kw, L/tau ratio
        D, L, tau, Li, isDuct, C0, Q, D2L = compute_main_dimension(Bav, ac, Kw, L_by_tau)
        # D, L, tau, Li, isDuct = compute_main_dimension(0.65, 20000, 0.95, 1.5)
        print('===============================================================')
        #print(D.m, L.m, Li.m, tau.m, isDuct)

        # Continue from here
        phi, Ts, Ss, yss, Zss, Kws, Cs, Kp, Kd = stator_design_winding(Bav, tau.m, L.m, D.m, Kw, qs)

        # phi, Ts, Ss, yss, Zss, Kws = stator_design_winding(0.65, 0.112, 0.167, 0.214, 0.95, 2)

        print(phi, Ts, Ss, yss.mm, Zss, Kws)

        phi, Ts, Ss, Zss, Bav, ac = adjust_initial_values(Zss, Ss, qs, Bav, ac, tau, L, Kw)

        Is, W2, Wsss, dss, Wts, Lmts, isCircular, h4, h3, h1, Bts, As, a, b, delta_s = stator_conductor_size_and_slot(phi, Ss, rating.poles, D, L, Li, tau, delta, Zss, space_factor, rect_matrix, swg_matrix)

        Acs, dcs, D0, Bcs = stator_core(phi, Li, D, dss)

        print('Stator Design Completed')
        print('===============================================================')

        lg, Dr = air_gap(L, D, air_gap_matrix)

        Sr, Ib, rotor_bar_area, Wsr, dsr, Btr_13, rotor_copper_loss, Lb, ysr, W0, Wsrr, h1, h3, h4, noAreaFound, delta_r, Rb, a_r, b_r = rotor_slots(Ss, Kws, Ts, Is, Dr, rect_matrix, phi, Li, L)

        total_rotor_copper_loss, slip, Ae, delta_e, De, Re, Ie, ring_copper_loss = end_rings_rotor(Sr, Ib, Dr, dsr, rotor_copper_loss)

        dcr, Bcr, Di = rotor_core(Dr, dcs, dsr, Bcs)

        print('Rotor Design Completed')
        print('===============================================================')

        s_W0 = Length(0.002)
        r_W0 = Length(0.0015)
        ATg = mag_air_gap(s_W0, r_W0, lg, yss, ysr, isDuct, rating.duct_width, L, D, 1, Bav, carter_matrix)
        ATs = mag_stator_teeth(Ss, Wts, Li, Bts, dss, lohys_bat_matrix)
        ATcs = mag_stator_core(D, Li, dcs, dss, Bcs, lohys_bat_matrix)
        ATr = mag_rotor_teeth(Btr_13, dsr, lohys_bat_matrix)
        ATcr = mag_rotor_core(Bcr, Li, Dr, dsr, dcs, dcr, lohys_bat_matrix)
        Im, AT60 = mag_no_load(Kws, Ts, ATg, ATs, ATcs, ATcr, ATr)
        loss_st = loss_stator_teeth(Ss, Wts, Li, dss, Bts, lohys_loss_matrix)
        loss_sc = loss_stator_core(D0, D, dss, Li, Bcs, lohys_loss_matrix)
        I0, phase_angle, currentCriterion, total_noload_loss, fw_loss, iron_loss, Il, no_load_pf = no_load_current(loss_st, loss_sc, Im, Is, fwloss_matrix)

        print('No Load Current Completed')
        print('===============================================================')

        slot_permeance_stator = stator_slot_leakage(Wsss, W2, W0, isCircular, h1, h3, h4)
        slot_permeance_rotor = rotor_slot_leakage(Wsss, W0, h1, h3, h4, Kws, Ss, Sr)
        X0 = overhang_leakage(yss, tau, Cs, Ss, Ts, qs, slot_leakage_matrix)
        xs = slot_leakage_reactance(slot_permeance_stator, slot_permeance_rotor, Ts, L, qs)
        Xm, Xs, Xz = total_leakage(Im, Ss, Sr, xs, X0)
        Rs, total_stator_copper_loss, rs, Rrs = resistance(Ts, As, Lmts, Is, total_rotor_copper_loss)
        Z, Isc, pf_sc, phase_sc, loss_fl, eff = Z_losses_eff(Rs, Xs, total_stator_copper_loss, total_rotor_copper_loss, total_noload_loss)

        print('Short Circuit Current Completed')
        print('===============================================================')

        theta = temperature_rise(iron_loss, total_stator_copper_loss, L, Lmts, D, D0, 80)

        print('Temperature Rise Completed')
        print('===============================================================')

        print("Bav                      : ", round(Bav,3))
        print("AC                       : ", ac)
        print("Efficiency (expected)    : ", 100*rating.efficiency)
        print("Efficiency (obtained)    : ", round(eff,1))
        print("Temperature Rise (degC)  : ", round(theta))
        print("Current Criterion        : ", currentCriterion)
        if ac >= 18000 and ac <= 24000 and currentCriterion and Bav >= 0.35 and Bav <= 0.6:
            break
        else:
            count += 10
            # print("Exit count: ", count)
            if count >= 6000:
                print("EXIT")
                if qs == 3:
                    if ac >= 24000 and ac <= 18000:
                        count = 0
                        continue
                    else:
                        break 
                if qs == 2:
                    qs = 3
                    count = 0 
            else:
                ac = 18000 + count
                # print(ac, Bav)
    print('===============================================================')
    if currentCriterion:
        print("Preparing design sheet...")
        mat = []
        mat.append(["RATING", "", str(""), ""])
        mat.append(["Full Load Output ", "", str(rating.power_in_kw), "kW"])
        mat.append(["Line Voltage", "", str(rating.line_voltage), "V"])
        mat.append(["Frequency", "f", str(rating.frequency), "Hz"])
        mat.append(["Phases", "", 3, ""])
        mat.append(["Efficiency", "eta", str(rating.efficiency) , ""])
        mat.append(["Power Factor", "cos(phi)", str(rating.power_factor), "lag"])
        mat.append(["No. of Poles", "p", str(rating.poles) , ""])
        mat.append(["Synchronous Speed", "ns", str(rating.rpm), "rpm"])
        mat.append(["KVA input", "", str(round(Q, 3)), "KVA"])
        mat.append(["Full load line current", "", str(round(Is, 3)), "A"])
        mat.append(["LOADING", "", str(""), ""])
        mat.append(["Specific Magnetic Loading", "Bav", str(round(Bav,3)), "Wb/m^2"])
        mat.append(["Specific Electric Loading", "ac", str(round(ac)), "A/m"])
        mat.append(["Output Coefficient", "", str(round(C0, 3)), ""])
        mat.append(["D2L", "", str(round(D2L,5)), "m^3"])
        mat.append(["MAIN DIMENSIONS", "", str(""), ""])
        mat.append(["Stator Bore", "D", str(round(D.mm, 1)), "mm"])
        mat.append(["Gross Iron Length", "L", str(round(L.mm, 1)), "mm"])
        mat.append(["Ducts", "nd", str(int(isDuct)), ""])
        mat.append(["Net Iron Length", "Li", str(round(Li.mm, 1)), "mm"])
        mat.append(["Pole pitch", "tau", str(round(tau.mm, 1)), "mm"])
        mat.append(["STATOR", "", str(""), ""])
        mat.append(["Type of Lamination", "", str("0.5mm thick Lohys"), ""])
        mat.append(["Type of Winding", "", str("Single Layer Mush"), ""])
        mat.append(["Connection", "", str("delta"), ""])
        mat.append(["Phase Voltage", "Eb", str(rating.line_voltage), "V"])
        mat.append(["Flux per pole", "phi_m", str(round(phi, 6)), "Wb"])
        mat.append(["Turns per phase", "Ts", str(Ts), ""])
        mat.append(["Number of Slots", "Ss", str(Ss), ""])
        mat.append(["Slots per pole", "", str(3*int(qs)), ""])
        mat.append(["Slots per pole per phase", "qs", str(qs), ""])
        mat.append(["Coil Span", "Cs", str(int(Cs)), "slots"])
        mat.append(["Distribution Factor", "Kd", str(round(Kd, 3)), ""])
        mat.append(["Pitch Factor", "Kp", str(round(Kp, 3)), ""])
        mat.append(["Winding Factor", "Kws", str(round(Kws, 3)), ""])
        mat.append(["Slot Pitch", "yss", str(round(yss.mm, 1)), "mm"])
        mat.append(["Conductors per slot", "Zss", str(Zss), ""])
        if isCircular:
            mat.append(["Conductor: bare diameter", "", str(round(a, 4)), "mm"])
            mat.append(["Conductor: insulated diameter", "", str(round(a+0.025, 4)), "mm"])
        else:
            mat.append(["Conductor: bare length", "", str(round(a, 4)), "mm"])
            mat.append(["Conductor: bare breadth", "", str(round(b, 4)), "mm"])
            mat.append(["Conductor: insulated length", "", str(round(a+0.025, 4)), "mm"])
            mat.append(["Conductor: insulated breadth", "", str(round(b+0.025, 4)), "mm"])
        mat.append(["Conductor: area", "", str(As.mm2), "mm^2"])
        mat.append(["Current density", "", str(round(delta_s,2)), "A/mm^2"])
        mat.append(["Length of mean turn", "Lmts", str(round(Lmts.m, 2)), "m"])
        mat.append(["Phase resistance at 25degC", "rs", str(round(rs,2)), "ohm"])
        mat.append(["Copper Loss at Full Load", "3I_s^2r_s", str(round(total_stator_copper_loss, 1)), "W"])
        mat.append(["Depth of stator core", "dcs", str(round(dcs.mm)), "mm"])
        mat.append(["Outer diameter of stator laminations", "De", str(round(D0.mm, 1)), "mm"])
        mat.append(["ROTOR", "", str(""), ""])
        mat.append(["Length of air gap", "la", str(round(lg.mm, 2)), "mm"])
        mat.append(["Diameter of rotor", "Dr", str(round(Dr.mm, 1)), "mm"])
        mat.append(["Type of winding", "", str("Squirrel Cage"), ""])
        mat.append(["Number of slots", "Sr", str(Sr), ""])
        mat.append(["Slots per pole per phase", "qr", str(round(Sr/(rating.phase*rating.poles), 3)), ""])
        mat.append(["Conductors per slot", "Zsr", str(1), ""])
        mat.append(["Winding factor", "Kwr", str(1), ""])
        mat.append(["Slot pitch", "ysr", str(round(ysr.mm,2)), "mm"])
        mat.append(["Rotor bar current", "Ib", str(round(Ib, 2)), "A"])
        mat.append(["Rotor bar: cross-section", "", str(a_r)+"x"+str(b_r), "mm^2"])
        mat.append(["Rotor bar: area", "ab", str(rotor_bar_area.mm2), "mm^2"])
        mat.append(["Rotor bar: length", "Lb", str(round(Lb.mm, 1)), "mm"])
        mat.append(["Rotor bar: current density", "delta_b", str(round(delta_r, 2)), "A/mm^2"])
        mat.append(["Resistance of each bar", "Rb", str(round(Rb*pow(10,6), 2))+" x 10^(-6)", "ohm"])
        mat.append(["Copper loss in bars", "S_r*I_b^2*r_b", str(round(rotor_copper_loss, 1)), "W"])
        mat.append(["End ring current", "Ie", str(round(Ie, 1)), "A"])
        mat.append(["End ring: cross-section", "", "10 x "+str(Ae.mm2//10), "mm^2"])
        mat.append(["End ring: area", "", str(Ae.mm2), "mm^2"])
        mat.append(["End ring: mean diameter", "De", str(round(De.mm, 1)), "mm"])
        mat.append(["End ring: current density", "delta_e", str(round(delta_e, 2)), "A/mm^2"])
        mat.append(["Resistance of each ring", "Re", str(round(Re*pow(10,6), 2))+" x 10^(-6)", "ohm"])
        mat.append(["Copper loss in end rings", "2*I_e^2*R_e", str(round(ring_copper_loss, 1)), "W"])
        mat.append(["Total rotor copper loss", "", str(round(total_rotor_copper_loss, 1)), "W"])
        mat.append(["Resistance of rotor (referred to stator)", "Rr", str(round(Rrs, 2)), "ohm"])
        mat.append(["Depth of rotor core", "dcr", str(dcr.mm), "mm"])
        mat.append(["NO LOAD CURRENT", "", str(), ""])
        mat.append(["Magnetizing mmf per pole", "", str(round(AT60, 1)), "A"])
        mat.append(["Phase magnetizing current", "Im", str(round(Im,1 )), "A"])
        mat.append(["Magnetising reactance", "Xm", str(round(Xm, 1)), "ohm"])
        mat.append(["Core loss", "", str(round(iron_loss, 1)), "W"])
        mat.append(["Friction and Windage Loss", "", str(round(fw_loss,1)), "W"])
        mat.append(["No load loss", "", str(round(total_noload_loss, 1)), "W"])
        mat.append(["Loss Component", "Il", str(round(Il, 3)), "A"])
        mat.append(["No load current (phase)", "Is", str(round(I0, 3)), "A"])
        mat.append(["No load current (line)", "", str(round(1.732*I0, 3)), "A"])
        mat.append(["No load power factor", "cos(phi_0)", str(round(no_load_pf, 3)), "lag"])
        mat.append(["SHORT CIRCUIT CURRENT", "", str(""), ""])
        mat.append(["Slot Leakage Reactance", "xs", str(round(xs, 3)), "ohm"])
        mat.append(["Overhang Leakage Reactance", "x0", str(round(X0, 3)), "ohm"])
        mat.append(["Zigzag Leakage Reactance", "xz", str(round(Xz, 3)), "ohm"])
        mat.append(["Total Leakage Reactance", "Xt", str(round(Xs, 3)), "ohm"])
        mat.append(["Total Resistance", "Rs", str(round(Rs, 3)), "ohm"])
        mat.append(["Short Circuit Impedance", "Zs", str(round(Z, 3)), "ohm"])
        mat.append(["Phase Short Circuit Current", "Isc", str(round(Isc, 3)), "A"])
        mat.append(["Line Short Circuit Current", "", str(round(1.732*Isc, 3)), "A"])
        mat.append(["Short Circuit p.f.", "cos(phi_sc)", str(round(pf_sc, 3)), "lag"])
        mat.append(["PERFORMANCE", "", str(""), ""])
        mat.append(["At full load: Losses", "", str(round(loss_fl, 1)), "W"])
        mat.append(["At full load: Output", "", str(round(1000*rating.power_in_kw, 1)), "W"])
        mat.append(["At full load: Input", "", str(round(1000*rating.power_in_kw + loss_fl, 1)), "W"])
        mat.append(["At full load: Efficiency", "eta", str(round(eff, 1)), "%"])
        # mat.append(["At full load: Power Factor", "", str(round(phase_sc, 3)), "lag"])
        mat.append(["At full load: Slip", "", str(round(100*slip, 2)), "%"])
        mat.append(["Temperature Rise", "theta_m", str(round(theta, 2)), "degC"])
        # mat.append(["", "", str(), ""])
        # mat.append(["", "", str(), ""])

        # print(numpy.array(mat))
        df_out = pandas.DataFrame(mat)
        df_out.to_excel("Design Sheet.xlsx", header=False, index=False)
        print("Design sheet successfully prepared!")
    else:
        print("Design sheet failed...")
    print('===============================================================')

def show_rating():
    print("Showing currently set ratings ")
    print()
    print("Power rating in kW   : ", rating.power_in_kw)
    print("Power factor         : ", rating.power_factor)
    print("Efficiency           : ", rating.efficiency)
    print("Speed in rpm         : ", rating.rpm)
    print("Line voltage in V    : ", rating.line_voltage)
    print('===============================================================')

def set_rating():
    importlib.reload(rating)