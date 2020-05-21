import pandas
import os

def load_table():
    package_directory = os.path.dirname(os.path.abspath(__file__))

    df_swg = pandas.read_excel(package_directory + '/lookupTables/SWG.xlsx')
    rect_swg = pandas.read_excel(package_directory + '/lookupTables/RectangularCopperConductor.xlsx', header=None)
    carter_coeff = pandas.read_excel(package_directory + '/lookupTables/Carter.xlsx', header=None)
    lohys_stamping = pandas.read_excel(package_directory + '/lookupTables/LohysBAT.xlsx', header=None)
    fwloss = pandas.read_excel(package_directory + '/lookupTables/fwloss.xlsx', header=None)
    lohys_loss = pandas.read_excel(package_directory + '/lookupTables/LohysLoss.xlsx', header=None)
    air_gap = pandas.read_excel(package_directory + '/lookupTables/AirGap.xlsx')
    slot_leakage = pandas.read_excel(package_directory + '/lookupTables/SlotLeakageTable.xlsx', header=None)

    swg_matrix = df_swg.values
    rect_matrix = rect_swg.values
    carter_matrix = carter_coeff.values
    lohys_bat_matrix = lohys_stamping.values
    fwloss_matrix = fwloss.values
    lohys_loss_matrix = lohys_loss.values
    air_gap_matrix = air_gap.values
    slot_leakage_matrix = slot_leakage.values

    print("Running...")
    return swg_matrix, rect_matrix, carter_matrix, lohys_bat_matrix, fwloss_matrix, lohys_loss_matrix, air_gap_matrix, slot_leakage_matrix

# s,t,u,v,w,x,y = load_table()
# df_swg = pandas.read_excel('os.getcwd()+/lookupTables/SWG.xlsx')