import numpy
from scipy.interpolate import interp1d

def getSpecificIronLoss(B, lohys_loss_matrix):
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
