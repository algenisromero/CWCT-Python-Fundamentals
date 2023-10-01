# Exercise 1-A
# print("Hello World!")

# Exercise 1-B
# my_text="Hello World!"
# print(my_text)

# Exercise 1-C
# some_txt1 = "Hello world!"
# some_txt2 = "The lone start state"
# number = 30
#
# print(some_txt1, some_txt2, number, sep="\n")

# Challenging

# Sine Wave Generator two sine waves 180 degrees out of phase
# y = Offset + A * sin(angle_in_radians)
import math
import time

A = 40
Offset = 40

for y in range(100):
    for x in range(0, 359, 15):
        radians = 2 * math.pi * x / 360
        index1 = int(Offset + (A * math.sin(radians)))
        # calculate a second index by adding PI to the angle_in_radians
        index2 = int(Offset + (A * math.sin(radians + math.pi)))
        line = ""
        for j in range(A*2 + 1):
            if j == index1 or j == index2:  # add OR comparison for the second index
                line = line + "*"
            else:
                line = line + " "
        print(line)
        time.sleep(0.1)
