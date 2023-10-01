##########################################################################
# Program Name: main.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M02 - Programming assignment
# Date: September 19, 2023,
#
# Description:
# Added a custom exception class for "NotNumericError" and the function for GetNumber() so that the
# Main program produces the following output:
#
# Error: A non-integer value was detected
# The input was not numeric!
##########################################################################

class NotNumericError(Exception):
    def __init__(self):
        print("Error: A non-integer value was detected")

def GetNumber(value):
        if value.isnumeric():
            return int(value)
        else:
            raise NotNumericError

print("Python Calculator")
print("This program will add, subtract, multiply or divide two integers")
print("Enter expression in form \"x <op> y\", e.g. 73 * 88")
calcmessage = input("Expression: ")
parameters = calcmessage.split()
try:
    value1 = GetNumber(parameters[0])
    operator = parameters[1]
    value2 = GetNumber(parameters[2])
except NotNumericError:
    print("The input was not numeric!")
    exit()
if operator == "+":
    result = value1 + value2
elif operator == "-":
    result = value1 - value2
elif operator == "*":
    result = value1 * value2
elif operator == "/":
    result = value1 / value2
print(value1, " ", operator, " ", value2, " = ", result)
