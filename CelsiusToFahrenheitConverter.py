# Celsius To Fahrenheit Converter

# Initialise input temperatures list (in Celsius)
celsius_list = []

# Initialise output temperatures list (in Fahrenheit)
fahrenheit_list = []

# Obtain list of input temperatures (integers, in Celsius)
while True:
    celsius_input = input("Enter each temperature, one by one, as a whole number (press Enter when finished): ")
    if celsius_input == "":
        break
    celsius_temp = int(celsius_input)
    celsius_list.append(celsius_temp)

for celsius in celsius_list:
    fahrenheit = celsius * 1.8 + 32
    fahrenheit_list = fahrenheit_list + [fahrenheit]

print("The temperatures in Fahrenheit are {}".format(fahrenheit_list))