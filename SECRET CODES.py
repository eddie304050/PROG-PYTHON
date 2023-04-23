# ******************************************************************************

# Author:           @eddie304050
# Program name:     Secret Codes (Functions)
# Date:             April 3th, 2022
# Purpose:          Create a python program to encode and decode a message
#                   using a cipher with a key value of 2.

# ******************************************************************************

# importing os module
import os

# Declaring variables and constants
KEY = 2
letter = ''
input_string = ""
encrypted_string = ""
decrypted_string = ""
choice = 0

#                             OUTPUT

# PROCESS

# User-defined function to encode message


def encode(input_string):
    encrypted_string = ""
    for letter_index in range(len(input_string)):
        letter = input_string[letter_index]
        # variable 'encrypted_string' stores encoded message
        encrypted_string += chr(ord(letter) + KEY)
    # Prints encoded message
    print("\nEncrypted message: ", encrypted_string)


# User-defined function to decode message
def decode(input_string):
    decrypted_string = ""
    for letter_index in range(len(input_string)):
        letter = input_string[letter_index]
        # variable 'decrypted_string' stores decoded message
        decrypted_string += chr(ord(letter) - KEY)
    # Prints decoded message
    print("\nDecrypted message: ", decrypted_string)


# Clears the terminal
os.system('cls')


print('*****************************************************************************')
print("                               SECRET CODES                                  ")
print('*****************************************************************************')


#                              INPUT


while True:
    print("\nEncode a Message: 1")
    print("Decode a message: 2")
    print("Exit: 3")
    choice = input('\nEnter your choice: ')

    # Prompts user to enter message to encode
    if str(choice) == '1':
        input_string = input("\nEnter message to be encoded: ")
        encode(input_string)

    # Prompts user to enter message to decode
    elif str(choice) == '2':
        input_string = input("\nEnter mesage to be decoded: ")
        decode(input_string)

    # Exits the program
    elif str(choice) == '3':
        # Clears the terminal
        os.system('cls')
        print("\n....Program Terminated.")
        break

    # Prompts user to enter valid input.
    else:
        print("\nPlease enter a valid integer(1-3). Try Again.")
        continue


# encrypted_string = ""
# for letter_index in range(len(input_string)):
# letter = input_string[letter_index]
# encrypted_string += chr(ord(letter) + key))
