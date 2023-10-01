# Triangle Wave Generator

import time

MaxY = 40
NumCycles = 10
Step = 4
PlotSymbol = "o"
EmptySymbol = " "

#Outer loop repeats number of cycles
for y in range(NumCycles):
    #inner loops draw the triangle wave
    for waveheight in range(0, MaxY, Step):
        line = ""
        #pad a string with spaces
        #put a "*" at the desired height
        #first loop ascends
        for i in range(MaxY):
            if i == waveheight: 
                line = line + PlotSymbol
            else:
                line = line + EmptySymbol
        print(line)
        time.sleep(0.05)

    #this loop descends
    for waveheight in range(0, MaxY, Step):
        line = ""
        for i in range(MaxY):
            if i == MaxY - waveheight - 1: 
                line = line + PlotSymbol
            else:
                line = line + EmptySymbol
        print(line)
        time.sleep(0.10)
 
 

# Sine Wave Generator
import math
import time

mag = 40
for y in range(100):
    for x in range(0, 360, 10):
        angle = 2 * math.pi * x / 360
        spaces = int(mag + (mag * math.sin(angle)))
        remain = (2 * mag) - spaces
        for j in range(spaces):
            print(" ", end="")
        print("*")
        time.sleep(0.05)


# Sine Wave Generator two sine waves 180 degrees out of phase
# y = A * sin(theta * t) + Offset
import math
import time

A = 40
Offset = 40

for y in range(100):
    for x in range(0, 359, 15):
        radians = 2 * math.pi * x / 360
        index1 = int(Offset + (A * math.sin(radians)))
        index2 = int(Offset + (A * math.sin(radians + math.pi)))
        line = ""
        for j in range(A*2 + 1):
            if j == index1 or j == index2: 
                line = line + "*"
            else:
                line = line + " "
        print(line)
        time.sleep(0.1)

