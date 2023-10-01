##########################################################################
# Program Name: distance_travel.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M03 - Triangles
# Date: August 29, 2023
#
# Description:
# This program asks the user for the speed of a vehicle (in miles per hour) and how many hours it has traveled.
# The program then use a loop to display the distance the vehicle has traveled for each hour of that
# time period. Here is an example of the output:
#
# What is the speed of the vehicle in mph? 40
# How many hours has it traveled? 3
#
# Hour  Distance Traveled
# --------------------------------
#  1           40
#  2           80
#  3          120
#
# Input Validation: Do not accept a negative number for speed and do not accept any value less than 1 for time traveled.
##########################################################################


# Get input from user
vehicle_speed = int(input("What is the speed of the vehicle in mph? "))
time_traveled = int(input("How many hours has it traveled? "))

# print table header
print("Hour       Distance Traveled-(Mph)")
print("-------------------------------------")

# verify for correct input and print table
if vehicle_speed <= 0 or time_traveled <= 0:
    print("Invalid inputs number must be greater than zero")
else:
    for t in range(time_traveled):
        distance = vehicle_speed * (t + 1)
        print(f" {t + 1}            {distance}")
