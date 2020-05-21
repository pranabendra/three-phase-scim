from scipy.interpolate import interp1d
import numpy

def getAirGapLength(diameter_from_main_dimension, air_gap_matrix):
    ans_air_gap = 0
    dia_column = air_gap_matrix[:,0]
    air_gap_column = air_gap_matrix[:,1]
    if diameter_from_main_dimension <= 0.15:
        ans_air_gap = 0.3
    elif diameter_from_main_dimension >= 0.8:
        ans_air_gap = 4
    else:
        f = interp1d(dia_column, air_gap_column)
        ans_air_gap = f(diameter_from_main_dimension).min()
    return ans_air_gap