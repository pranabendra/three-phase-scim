class Length:
    m = 0
    mm = 0
    def __init__(self, length_in_meter):
        self.m = length_in_meter
        self.mm = pow(10,3)*length_in_meter
    def setLength(self, length_in_meter):
        self.m = length_in_meter
        self.mm = pow(10,3)*length_in_meter

class Area:
    m2 = 0
    mm2 = 0
    def __init__(self, area_in_meter_square):
        self.m2 = area_in_meter_square
        self.mm2 = pow(10,6)*area_in_meter_square
    def setArea(self, area_in_meter_square):
        self.m2 = area_in_meter_square
        self.mm2 = pow(10,6)*area_in_meter_square
