import os
import pandas
import numpy
from scipy.interpolate import interp1d

package_dir = os.path.dirname(os.path.abspath(__file__))

fwloss_df = pandas.read_excel(package_dir+'/lookupTables/fwloss.xlsx', header=None)
fwloss_matrix = fwloss_df.values

def getFrictionWindageLoss(power_rating):
    ans_fwloss = 0
    power_column = fwloss_matrix[:,0]
    perc_column = fwloss_matrix[:,1]
    if power_rating <= 0.75:
        ans_fwloss = 5.5
    elif power_rating >= 150:
        ans_fwloss = 1
    else:
        f = interp1d(power_column, perc_column)
        ans_fwloss = f(power_rating).min()
    return ans_fwloss

print(getFrictionWindageLoss(2.98))