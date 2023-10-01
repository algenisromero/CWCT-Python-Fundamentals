"""
Author: Algenis Romero
Course: Introduction to Python for Cybersecurity (CWCT-140)
Date: August 21, 2023
Program Name: weights.py
Description:
Create a simple Python “calculator” this program will add, subtract, divide or multiple
two numbers. Ensure expresion is in the form 'x <op> y', e.g 7 * 8

"""

print("Python Calculator")
print("This program will add, subtract, divide or multiple two numbers.")
print("Type:\n + for Add.\n - for Subtract.\n / for Divide. \n * for Multiply.")

# Prompt user for a input
expression = input("Enter expression in form \"x <op> y\", e.g. 73 * 80: ")

# Input the “expression” into a variable named “calcmessage”
calc_message = expression.split()

# Split the string into its pieces – see code below
val1 = int(calc_message[0])
operator = calc_message[1]
val2 = int(calc_message[2])

# Populate the “if then else” chain with the proper statements – see code below
match operator:
    case "+":
        result = val1 + val2
    case "-":
        result = val1 - val2
    case "*":
        result = val1 * val2
    case "/":
        result = val1 / val2
    case _:
        print("Invalid input!! Please enter in the form \"23 + 56\"")

# Print the answer as shown at the top
print(f"{val1} {operator} {val2} = {result}")