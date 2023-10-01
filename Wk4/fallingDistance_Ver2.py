# Falling version 2
# Instructor solution

def fallingDistance(time):
    return 0.5 * 9.8 * (time ** 2)


for d in range(3):
    time = (d + 1) * 5
    print(str(time) + "\t" + str(round(fallingDistance(time), 2)))

# TODO if input is less than 5, code only print distance from 5 and up.