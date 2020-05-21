import os
import pandas
import numpy
from scipy.interpolate import interp1d

package_dir = os.path.dirname(os.path.abspath(__file__))

carter_coeff = pandas.read_excel(package_dir+'/lookupTables/Carter.xlsx')
carter_matrix = carter_coeff.values

def getCarterCoeff(typeOfSlot, ratio):
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

print(getCarterCoeff('semiClosed', 4.8))