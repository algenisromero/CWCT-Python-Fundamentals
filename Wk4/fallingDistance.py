##########################################################################
# Program Name: fallingDistance.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M04 - Falling Distance
# Date: September 7, 2023
#
# Description:
# This code contains a function named fallingDistance that accepts an object’s falling time (in seconds) as an argument.
# The function return the distance, in meters, that the object has fallen during that time interval.
# The program prompting the user for the total time and calling the function in a loop that passes the time values in 5
# second increments as the argument and displays the elapsed time and return value.
##########################################################################

# Function to calculate the falling distance
def fallingDistance(time):
    GRAVITY = 9.8
    distance = 0.5 * GRAVITY * (time ** 2) # Formula
    return distance

# Prompt user for input time in secods.
time = int(input("Enter time in seconds: "))

# Verify user input and print info if number not greater than ten.
if time < 10:
    print("Input a number equal or greater than 10!!!")
else:
    # Print a table with fall distance in a time increment of 5 seconds
    print("Time(Secs)   Distance(Meters)")
    for t in range(0, int(time), 5):
        d = round(fallingDistance(t), 2)
        print(f"{t : >4}            {d}")
