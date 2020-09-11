# This is an Investment Calculator built in Python 3.7.0
# Coded by Kyle Spencer

from math import *

# Variable Declaration
years = 0
current_principal = 0
monthly_invest = 0
yearly_invest = 0
interest_rate = 0
final_total = 0

# Main Program
print("Welcome to Investment_Calc: Python!")

current_principal = input("Please enter your starting principal: ")
current_principal = float(current_principal)

monthly_invest = input("How much are you investing each month? ")
monthly_invest = float(monthly_invest)
yearly_invest = monthly_invest * 12

years = input("How many years are you planning to invest for? ")
years = int(years)

interest_rate = input("What do you estimate will be the yearly interest of your investments? (10% = 0.1) ")
interest_rate = float(interest_rate)

print("\n")

for i in range(years):
    if final_total == 0:
        final_total = current_principal
    
    final_total = (final_total + yearly_invest) * (1 + interest_rate)

final_total = round(final_total)

print("You would have " + str(final_total) + " after " + str(years) + " years.")
print("Thank you for using Investment_Calc: Python!")
