from scipy.interpolate import interp1d
import numpy

def getOverhangLeakage(ratio, slot_leakage_factor_matrix):
    ans_ratio = 0
    ratio_cs_pp_column = slot_leakage_factor_matrix[:,0]
    slot_leakage_factor_column = slot_leakage_factor_matrix[:,1]
    if ratio <= 0.5:
        ans_ratio = 0.5
    elif ratio >= 1:
        ans_ratio = 1
    else:
        f = interp1d(ratio_cs_pp_column, slot_leakage_factor_column)
        ans_ratio = f(ratio).min()
    return ans_ratio