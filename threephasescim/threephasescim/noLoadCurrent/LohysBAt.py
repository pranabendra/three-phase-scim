from scipy.interpolate import interp1d
import numpy

def getATFromLohys(B, lohys_bat_matrix):
    ans_lohys_bat = 0
    B_column = lohys_bat_matrix[:,0]
    At_column = lohys_bat_matrix[:,1]
    if B <= 0:
        ans_lohys_bat = 0
    elif B >= 2:
        ans_lohys_bat = 25000 + 9000*(B-2)/0.1
    else:
        f = interp1d(B_column, At_column)
        ans_lohys_bat = f(B).min()
    return ans_lohys_bat