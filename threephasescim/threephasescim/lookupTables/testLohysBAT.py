import os
import pandas
import numpy
from scipy.interpolate import interp1d

package_dir = os.path.dirname(os.path.abspath(__file__))

lohys_bat_df = pandas.read_excel(package_dir+'/lookupTables/LohysBAT.xlsx')
lohys_bat_matrix = lohys_bat_df.values

def getATFromLohys(B):
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

print(getATFromLohys(1.2))