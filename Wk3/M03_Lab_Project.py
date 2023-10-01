##########################################################################
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Date: August 21, 2023
# Program Name: weights.py
# Description:
# This code accept a data list and does the work of printing the bar graphs
##########################################################################

# Function to plot bar graphs
def plotBars(data_list, plotsymbil):
    # Use a for loop to print 40 blank lines
    # this "clears" out the console windows
    for b in range(2):
        print()
    # for each value in the list print "value" using string replication
    for val in data_list:
        print(val * plotsymbil)

def bubbleSort(sorted_list):
    for outer_index in range(len(sorted_list)):
        # Sort subroutine
        for inner_index in range(0, len(sorted_list) - outer_index - 1):
            if sorted_list[inner_index] > sorted_list[inner_index + 1]:
                temp = sorted_list[inner_index]
                sorted_list[inner_index] = sorted_list[inner_index + 1]
                sorted_list[inner_index + 1] = temp
        plotBars(sorted_list, "*")


# Data list
thelist = [50, 40, 30, 20, 10, 5, 4, 3, 2, 1]

# Call the function and print the bars.
bubbleSort(thelist)
print("The data was: ", thelist)
print()