import os
import pandas
import numpy
from scipy.interpolate import interp1d

package_dir = os.path.dirname(os.path.abspath(__file__))

lohys_loss_df = pandas.read_excel(package_dir+'/lookupTables/LohysLoss.xlsx')
lohys_loss_matrix = lohys_loss_df.values

def getSpecificIronLoss(B):
    ans_lohys_loss = 0
    B_column = lohys_loss_matrix[:,0]
    specific_column = lohys_loss_matrix[:,1]
    if B <= 0:
        ans_lohys_loss = 0
    elif B >= 1.8:
        ans_lohys_loss = 13 + 3.7*(B-1.8)/0.2
    else:
        f = interp1d(B_column, specific_column)
        ans_lohys_loss = f(B).min()
    return ans_lohys_loss

print(getSpecificIronLoss(2))