##########################################################################
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Date: August 21, 2023
# Program Name: restaurant.py
# Description:
# This code informs a user of their total meal charges, shows a suggested tip and
# request a tip amount. Code print the total bill.
##########################################################################
# Prompt the user for the amount of the meal (e.g. $32.95).
# Compute the tax on the restaurant bill. The tax should be 6.75 percent of the meal cost.
# Prompt the user for the tip amount (Suggesting a value equal to 18 percent of the total).
# Display the meal cost, tax amount, tip amount, and total bill on the screen.
##########################################################################

TAX = 0.0675
SUGGESTED_TIP = 0.18

print("----------------- R E S T A U R A N T -----------------")
meal_cost = float(input("Type your bill amount: $ "))

print("------------------------ T I P ------------------------")
tip_amount = meal_cost * SUGGESTED_TIP
bill_with_tip = meal_cost + tip_amount
print("Suggested tip of 18%: $", round(tip_amount, 2))
print(f"Your bill is ${meal_cost} with 18% tip will be $", round(bill_with_tip, 2))
tip = float(input("Please input your tip amount: $ "))


print("------------------------ T O T A L ------------------------")
bill_tax = meal_cost * TAX
total_bill = meal_cost + bill_tax + tip
print("Tax: $", round(bill_tax, 2))
print("Your total bill is: $", round(total_bill, 2))

