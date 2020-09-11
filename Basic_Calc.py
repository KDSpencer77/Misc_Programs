# This is a Basic Calculator built in Python 3.7.0
# Coded by Kyle Spencer

from math import *

# Function Definition
def add(num_1, num_2):
    result = num_1 + num_2
    return result

def subtract(num_1, num_2):
    result = num_1 - num_2
    return result

def multiply(num_1, num_2):
    result = num_1 * num_2
    return result

def divide(num_1, num_2):
    result = num_1 / num_2
    return result

# Variable Definition
choice = 0
first_number = 0
second_number = 0
result = 0

# Main Program
print("Welcome to Basic_Calc: Python!")
print("Here are your options:")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("\n")

choice = input("What would you like to choose?")
choice = float(choice)

if choice == 1:
    print("You have chosen Addition")
    first_number = input("What is your first number? ")
    second_number = input("What is your second number? ")

    result = add(float(first_number), float(second_number))
    print("Your result is " + str(result) + ".")
    print("Thank you for using Basic_Calc: Python")

elif choice == 2:
    print("You have chosen Subtraction")
    first_number = input("What is your first number? ")
    second_number = input("What is your second number? ")

    result = subtract(float(first_number), float(second_number))
    print("Your result is " + str(result) + ".")
    print("Thank you for using Basic_Calc: Python")

elif choice == 3:
    print("You have chosen Multiplication")
    first_number = input("What is your first number? ")
    second_number = input("What is your second number? ")

    result = multiply(float(first_number), float(second_number))
    print("Your result is " + str(result) + ".")
    print("Thank you for using Basic_Calc: Python")

elif choice == 4:
    print("You have chosen Division")
    first_number = input("What is your first number? ")
    second_number = input("What is your second number? ")

    result = divide(float(first_number), float(second_number))
    print("Your result is " + str(result) + ".")
    print("Thank you for using Basic_Calc: Python")

elif choice == 69:
    print("Nice!")

else:
    print("You have entered an invalid selection.")
    print("Thank you for using Basic_Calc: Python")
