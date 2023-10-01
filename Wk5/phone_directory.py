##########################################################################
# Program Name: phone_directory.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M04 - Area of a Circle
# Date: September 15, 2023,
#
# Description:
# The program created, viewed and managed entries in the directory using a python dictionary object.
##########################################################################
import csv

#  Function to read data in a file
def readCSV(csvFile):
    phone_dir = {}
    with open(csvFile, mode='r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for row in reader:
            phone_dir[row[0]] = row[1]
    return phone_dir

# Function to write data in file

def writeCSV(csvFile, phone_dir, column1, column2):
    with open(csvFile, mode='w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerow([column1, column2])
        for item in phone_dir:
            writer.writerow([item, phone_dir[item]])


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
    for key, value in phone_directory.items():
        print(f"{key:8}{value}")
    print("-----------------------")


# Function to add new contact
def add_contact():
    print("\n")
    name = input("Type name: ")
    phone = input("Type phone: ")
    if not name in phone_directory:
        phone_directory[name] = phone
        writeCSV(phone_list_filepath, phone_directory, "name", "number")
        print("--------------------------")
        print(f"{name}-{phone} added!!!")
        print("--------------------------")
    else:
        print(f"{name} already exist!!")
    # phone_directory[name] = phone


# Function to delete a contact
def delete_contact():
    print("\n")
    name = input("Type name to delete: ")
    if name in phone_directory:
        del_value = phone_directory.pop(name)
        writeCSV(phone_list_filepath, phone_directory, "name", "number")
        print("--------------------------------")
        print(f"{name}-{del_value} deleted!!!")
        print("--------------------------------")
    else:
        print(f"{name} not found!!")


# Function to update contact
def update_contact():
    print("\n")
    name = input("Type name to update: ")
    phone = input("Type new phone number: ")
    if name in phone_directory:
        phone_directory[name] = phone
        writeCSV(phone_list_filepath, phone_directory, "name", "number")
        print("--------------------------------")
        print(f"{name}-{phone} updated!!!")
        print("--------------------------------")
    else:
        print(f"{name} not found!!")


phone_list_filepath = "contact_db.csv"
phone_directory = readCSV(phone_list_filepath)

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
        print("Exiting phone book.....")  # Exit program
        break
