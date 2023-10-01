##########################################################################
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Date: August 21, 2023
# Program Name: weights.py
# Description:
# This code can calculate an individual's weight on another planet by multiplying their weight times
# the relative surface gravity of the other world.
##########################################################################
# Weight on Other Planet = Weight on Earth x Multiple of Earth’s Gravity
#
# Design a Python program that asks a user for their name and weight. The program will greet the user
# by name and then calculate/display the user's weight on the other planets.
# Each item should be displayed on a line by itself.
#
# Use the following values for the conversions
#
# Body Multiple of Earth’s Gravity
# Sun 27.01
# Mercury 0.38
# Venus 0.91
# Earth 1 (defined)
# Moon 0.166
# Mars 0.38
# Jupiter 2.34
# Saturn 1.06
# Uranus 0.92
# Neptune 1.19
# Pluto 0.06
##########################################################################

name = input("What is your name? ")
print(f"Hello, {name}.")
print("let's check your weight in others planet, ready!!!")
user_weight = float(input("Tell me your weight in lbs: "))
# formatted_weight = round(user_weight, 2)

print("Your weight in the following planets are:")
print("Sun - ", round(27.01 * user_weight, 2))
print("Mercury - ", round(0.38 * user_weight, 2))
print("Venus - ", round(0.91 * user_weight, 2))
print("Earth - ", round(1 * user_weight, 2))
print("Moon - ", round(0.166 * user_weight, 2))
print("Mars - ", round(0.38 * user_weight, 2))
print("Jupiter - ", round(2.34 * user_weight, 2))
print("Saturn - ", round(1.06 * user_weight, 2))
print("Uranus - ", round(0.92 * user_weight, 2))
print("Neptune - ", round(1.19 * user_weight, 2))
print("Pluto - ", round(0.06 * user_weight, 2))