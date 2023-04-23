# Author:       @eddie304050
# Date:         March 6, 2022
# Description:  In this program we take a value from the user,
#               and list the prime numbers till that value.


# declaring variables, lists, constants
import math
limit = 0
prime = 0
divisor = 0
prime_list = []
LOWER_LIMIT = 2
UPPER_LIMIT = 71
CONSTANT_X = 'X'
SMALLEST_PRIME = 2


print('*************************************************************')
print("                   PRIME NUMBER FINDER                       ")
print('*************************************************************')

# importing math module

# INPUT

# prompt the user to input limiter value and store into variable 'LIMIT'
limit = input('Enter a limit to the prime number you want displayed: ')


# check wether input is valid
# if not, print appropriate error message and prompt user to try again
while True:
    if limit.isnumeric() == True:
        if int(limit) > 2 and int(limit) < 71:
            break
        elif int(limit) < 2 or int(limit) > 71:
            limit = input("Limit must be 2 to 70 inclusive. Try Again: ")
            continue
    elif limit.isdecimal() == True:
        limit = input("Limit must be a whole number. Try Again: ")
        continue
    else:
        limit = input("Limit must be a whole number. Try Again: ")
    continue


# PROCESS

# take all prime numbers from 2-70
# store in list 'prime_list'
for prime in range(LOWER_LIMIT, UPPER_LIMIT):
    if prime > 1:
        for divisor in range(SMALLEST_PRIME, prime):
            if prime % divisor == 0:
                break
        else:
            prime_list.append(prime)


# OUTPUT

# print prime values till the limit along with same number of 'X' characters
for prime in prime_list:
    if int(prime) <= int(limit):
        print(prime * CONSTANT_X, "", prime)


# prompt user to press ENTER to exit
input("Press ENTER to exit")
