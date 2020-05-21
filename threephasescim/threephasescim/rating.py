# Anwesa
# power_in_kw = 20
# power_factor = 0.82
# efficiency = 0.85
# rpm = 1000
# line_voltage = 415

# Pranabendra
# power_in_kw = 2.98
# power_factor = 0.84
# efficiency = 0.85
# rpm = 1500
# line_voltage = 415

# power_in_kw = 8
# power_factor = 0.83
# efficiency = 0.8
# rpm = 1500
# line_voltage = 415

# power_in_kw = 5.22
# power_factor = 0.83
# efficiency = 0.83
# rpm = 1000
# line_voltage = 415

# power_in_kw = 3
# power_factor = 0.83
# efficiency = 0.8
# rpm = 1500
# line_voltage = 415

# power_in_kw = 30
# power_factor = 0.85
# efficiency = 0.85
# rpm = 1500
# line_voltage = 110

# power_in_kw = 8.95
# power_factor = 0.83
# efficiency = 0.8
# rpm = 1500
# line_voltage = 415

# power_in_kw = 15
# power_factor = 0.82
# efficiency = 0.85
# rpm = 1500
# line_voltage = 415

####################
# Bodhisatya
# power_in_kw = 25
# power_factor = 0.85
# efficiency = 0.85
# rpm = 3000
# line_voltage = 415

# # Vishal
# power_in_kw = 5
# power_factor = 0.83
# efficiency = 0.8
# rpm = 1500
# line_voltage = 400

# # Abhrajit
# power_in_kw = 37.3
# power_factor = 0.85
# efficiency = 0.85
# rpm = 1000
# line_voltage = 415

# Jayanta
# power_in_kw = 8.95
# power_factor = 0.83
# efficiency = 0.8
# rpm = 1000
# line_voltage = 110

# Ramij
# power_in_kw = 50
# power_factor = 0.85
# efficiency = 0.85
# rpm = 1000
# line_voltage = 415

# Sayan
# power_in_kw = 8
# power_factor = 0.83
# efficiency = 0.8
# rpm = 1000
# line_voltage = 415

print("Enter the following ratings below")
print()
power_in_kw = float(input(  "Enter power rating in kW   : "))
power_factor = float(input( "Enter power factor         : "))
efficiency = float(input(   "Enter efficiency           : "))
rpm = float(input(          "Enter speed in rpm         : "))
line_voltage = float(input( "Enter line voltage in V    : "))


Kw = 0.95

phase = 3
frequency = 50

ns = rpm/60
poles = (2*frequency)/ns

duct_exceed_length = 120/1000
duct_width = 10/1000