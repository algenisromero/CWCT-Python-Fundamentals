##########################################################################
# Program Name: CaesarCipher.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M04 - Function Lab
# Date: September 7, 2023
#
# Description:
# A function that can encrypt and decrypt a text message using a Caesar encryption.
##########################################################################

# Create Function
def caesar(message, key):
    message_to_cypher = ""
    # Traverse text
    for char in message:
        if char == " ":
            message_to_cypher += " "
        elif char.upper():
            message_to_cypher += chr((ord(char) + key - 65) % 26 + 65)
        else:
            message_to_cypher += chr((ord(char) + key - 97) % 26 + 97)

    return message_to_cypher

string = input("Enter message: ")
key = int(input("Enter encryption key: "))

encrypted = caesar(string,key)
print("Encrypted message: ", encrypted)

dencrypted = caesar(encrypted,-key)
print("Decrypted message: ", dencrypted)




