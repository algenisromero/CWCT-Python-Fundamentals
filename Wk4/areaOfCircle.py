##########################################################################
# Program Name: areaOfCircle.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M04 - Area of a Circle
# Date: September 7, 2023
#
# Description:
# This program prompts the user to enter the center and a point on the circle (two tuples containing an x and y value).
# The program then output the circle’s radius, diameter, circumference, and area.
##########################################################################
import math

# Function to calculate the radius
def calculateRadius(x1, x2, y1, y2):
    return ((x2-x1) ** 2 + (y2-y1)** 2) ** (1/2)

# Function to calculate the area
def calculateArea():
    return math.pi * calculateRadius(x1, x2, y1, y2) ** 2

# Function to calculate the perimeter
def calculatePerimeter():
    return 2 * math.pi * calculateRadius(x1, x2, y1, y2)

# Prompt user to input center of the circle (x1,y1)
x1 = float(input("Enter the x coordinate of the center of the circle: "))
y1 = float(input("Enter the y coordinate of the center of the circle: "))

# Prompt user to input a point of the circle (x2,y2)
x2 = float(input("Enter the x coordinate of the point on the circle: "))
y2 = float(input("Enter the y coordinate of the center on the circle: "))

# Calculate the radius of the set of input points
radius = calculateRadius(x1, x2, y1, y2)

# Print the radius, area and perimeter of the circle
print("Your circle radius is: ", round(radius))
print("Circle area is: ", round(calculateArea(),2))
print("Circle perimeter: ", round(calculatePerimeter(),2))