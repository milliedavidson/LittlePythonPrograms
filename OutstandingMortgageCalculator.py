# Outstanding Mortgage Calculator

# Mortgage amount left, as a positive number
mortgage = float(input("What is the mortgage amount left to pay? "))

# Monthly mortgage payment, as a positive integer
payment = float(input("What is the monthly mortgage payment? "))

# Annual interest rate, as a floating-point percentage
while True:
    rate = input("What is the annual interest rate on the mortgage? ")
    try:
        rate = float(rate) / 100  # divide by 100 to convert percentage to decimal
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the interest rate.")

# Calculate outstanding amount
interest = mortgage * (rate / 12)  # monthly interest rate
outstanding = mortgage + interest - payment

print("The outstanding mortgage is: {}.".format(outstanding))