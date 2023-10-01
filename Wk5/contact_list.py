##########################################################################
# Program Name: contact_list.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M04 - Area of a Circle
# Date: September 9, 2023
#
# Description:
# This program provides a menu-driven digital contact list to the user. By creating a dictionary with four or five
# contacts (names and numbers). The user is able to add/update/delete entries to the contact list.
##########################################################################

# Initial dictionary data
contact_lst = {"Mike":"555-254-0978",
               "John":"220-456-3421",
               "Viela":"767-911-4532",
               "Nu":"435-456-1245"
               }
# User menu options function.
def menu():
    print("\n       PHONE BOOK MENU")
    print("---------------------------------")
    print("Option 1: View contact list.")
    print("Option 2: Add a new contact.")
    print("Option 3: Delete a contact.")
    print("Option 4: Update contact.")
    print("Option 0: Exit.")
    print("---------------------------------\n")

# Function to list all contacts
def show_contacts():
    print("\n")
    print("Name       Phone")
    print("-----------------------")
    for key, value in contact_lst.items():
        print(f"{key:8}{value}")
    print("-----------------------")

# Function to add new contact
def add_contact():
    print("\n")
    name = input("Type name: ")
    phone = input("Type phone: ")
    contact_lst[name] = phone
    print("--------------------------")
    print(f"{name}-{phone} added!!!")
    print("--------------------------")

# Function to delete a contact
def delete_contact():
    print("\n")
    name = input("Type name to delete: ")
    del_value = contact_lst.pop(name, "Contact not found!!")
    print("--------------------------------")
    print(f"{name}-{del_value} deleted!!!")
    print("--------------------------------")

# Function to update contact
def update_contact():
    print("\n")
    name = input("Type name to update: ")
    phone = input("Type new phone number: ")
    contact_lst[name] = phone
    print("--------------------------------")
    print(f"{name}-{phone} updated!!!")
    print("--------------------------------")

# Loop to show menu until user type zero for exit
while True:
    menu()
    menu_opt = int(input("Type your option: "))
    # Verify user input and call function.
    if menu_opt == 1:
        show_contacts()
    elif menu_opt == 2:
        add_contact()
    elif menu_opt == 3:
        delete_contact()
    elif menu_opt == 4:
        update_contact()
    else:
        print("Exiting phone book.....") # Exit program
        break





