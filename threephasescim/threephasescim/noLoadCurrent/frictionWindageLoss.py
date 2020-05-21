from scipy.interpolate import interp1d
import numpy

def getFrictionWindageLoss(power_rating, fwloss_matrix):
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
