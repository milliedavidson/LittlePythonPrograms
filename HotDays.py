# Hot days - Find temperatures above 30 degrees (Celsius)

# Initialise list of input temperatures
recorded_temps = []

# Initialise list of output temperatures
hot_days = []

# Obtain list of input temperatures (integers, in Celsius)
while True:
    temp_input = input("Enter each temperature as a whole number (press Enter when finished): ")
    if temp_input == "":
        break
    temp = int(temp_input)
    recorded_temps.append(temp)

for temperature in recorded_temps:
    if temperature > 30:
        hot_days = hot_days + [temperature]

print("The hot days had the temperatures {}".format(hot_days))