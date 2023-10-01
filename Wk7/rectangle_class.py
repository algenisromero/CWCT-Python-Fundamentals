##########################################################################
# Program Name: rectangle_class.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M07 - Lab Project
# Date: September 28, 2023,
#
# Description:
# The program calculate and modified the area of a rectangle
##########################################################################

# Create a class Rectangle
class Rectangle:
    # constructor for the class that receives the length and width
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # Mutator methods setLength, and setWidth that allow the attributes of the rectangle to be changed.
    def setLength(self, length):
        self._length = length

    def setWidth(self, width):
        self._width = width

    # getArea method that will return the area of the rectangle
    def getArea(self):
        return self._length * self._width

    # the __str__  method to display the rectangle’s information
    def __str__(self):
        return "Length: " + str(self._length) + "\nWidth: " + str(self._width) + "\nArea: " + str(self.getArea())


# Main program that utilizes the Rectangle class
print("Calculate Rectangle Area")
length = float(input("Enter your length: ")) # Prompt the user for the length
width = float(input("Enter your width: ")) # a.	Prompt the user for the width

myRectangle = Rectangle(length, width) # Create an object for the Rectangle
print(myRectangle) # Using the __str__ Method, display the rectangle’s information

# Allow the user to change/set the length and width
new_length = float(input("Enter your new length: "))
new_width = float(input("Enter your new width: "))
myRectangle.setLength(new_length)
myRectangle.setWidth(new_width)

# Display the rectangle’s attributes (print the rectangle)
# after the rectangle has been changed using the appropriate methods.
print("Modified rectangle:\n", myRectangle)