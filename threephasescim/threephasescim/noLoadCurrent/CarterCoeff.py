from scipy.interpolate import interp1d
import numpy

def getCarterCoeff(typeOfSlot, ratio, carter_matrix):
    ans_carter = 0
    if typeOfSlot == 'semiClosed':
        semi_closed_column = carter_matrix[:,1]
        ratio_column = carter_matrix[:,0]
        if ratio <= 0:
            ans_carter = 0
        elif ratio >= 12:
            ans_carter = 0.95
        else:
            f = interp1d(ratio_column, semi_closed_column)
            ans_carter = f(ratio).min()
    elif typeOfSlot == 'open':
        open_column = carter_matrix[:,2]
        ratio_column = carter_matrix[:,0]
        if ratio <= 0:
            ans_carter = 0
        elif ratio >= 12:
            ans_carter = 0.72
        else:
            f = interp1d(ratio_column, open_column)
            ans_carter = f(ratio).min()
    else:
        print("Mayday...")
    return ans_carter
