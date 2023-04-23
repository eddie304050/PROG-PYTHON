# Author:        @eddie304050
# Date:          January 27,2022
# Description:   A python program that takes the user's 
#                height and weight, and provides their BMI as output.

# Declaring variables and constants

height = 0.0 # variable to hold user height
weight = 0.0 # variable to hold user weight
bmi = 0.0 # variable to hold result value
CONSTANT_VALUE = 703 # constant used in the BMI equation

# INPUT

# Prompt the user to enter their height in inches
# Store the value in variable "height" as float data type
height = float(input("Enter the person's height in inches:"))

# Prompt the user to enter their weight in pounds
# Store the input in variable "weight" as float data type
weight = float(input("Enter the person's weight in pounds:"))

# PROCESS

# Run the inputs through the equation for BMI
# Assign resulting value to variable "BMI"
bmi = (weight / height**2) * CONSTANT_VALUE

# OUTPUT

# Display the result with 1 decimal point in a formatted string 
# along with the user inputs
print("\nA person who is " + str(height) + " inches tall and weighs " + str(weight) + " pounds has a BMI of " + str(round(bmi,1)))

#Prompt the user to press ENTER to exit
input("\nPress ENTER to exit..")
