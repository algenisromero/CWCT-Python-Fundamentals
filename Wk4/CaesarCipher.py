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

# Creating Function
def CaesarCipher(string, key):
    encrypt_txt = ""
    # Traverse text
    for c in string:
        # Get letter value
        letter_value = ord(c)
        letter_value = letter_value + key
        # Check for non-printable characters
        if letter_value < 32:
            letter_value = letter_value + 95
        elif letter_value > 126:
            letter_value = letter_value - 95
        # Cipher text
        encrypt_txt = encrypt_txt + chr(letter_value)
    return encrypt_txt

# Print a title header
print("Secret Message Encoder")
print("------------------------")
# Get inputs from user
string = input("Enter message: ")
key = int(input("Enter encryption key: "))

# Call function and print encrypted
encrypted = CaesarCipher(string, key)
print("Encrypted message: ", encrypted)

# Call function and print decrypted
decrypted = CaesarCipher(encrypted, -key)
print("Decrypted message: ", decrypted)




