##########################################################################
# Program Name: triangle.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M03 - Triangles
# Date: August 28, 2023
#
# Description:
# This program prompts the user to enter the lengths of three sides of a triangle.
# The program will output a message indicating whether the lengths form a triangle and, if so,
# whether the triangle is a right triangle, an isosceles triangle, and/or an equilateral triangle.
##########################################################################

# Asking for side lengths
side_one = int(input("Type the length of your first side: "))
side_two = int(input("Type the length of your second side: "))
side_three = int(input("Type the length of your third side: "))

# Verify is triangle is valid and print type of triangle.
if side_one + side_two >= side_three and side_two + side_three >= side_one and side_three + side_one >= side_two:
    print("Makes a triangle!")
    if side_one == side_two and side_two == side_three:
        print("Equilateral triangle")
    elif side_one == side_two or side_two == side_three or side_one == side_three:
        print("Isosceles triangle")
    else:
        print("Right triangle")
elif side_one == 0 or side_two == 0 or side_three == 0:
    print("Invalid input, type numbers greater than zero!!")
    if side_one == side_two and side_two == side_three:
        print("Equilateral triangle")
    elif side_one == side_two or side_two == side_three or side_one == side_three:
        print("Isosceles triangle")
    else:
        print("Right triangle")
else:
    print("Does not make a triangle.")
