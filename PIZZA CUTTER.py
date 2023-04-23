# Author:       Edwin Abraham
# Date:         February 12, 2022
# Description:  This program accepts diameter of pizza in inches from user,
#               and then calculates the area of 1 slice of pizza with that diameter.


# Declaring Variables and Constants
import math
input_diameter = 0
number_slices = 0
area_slice = 0
radius = 0

# Use math module


try:
    # Prompt user to enter diameter of pizza and check if input is valid
    input_diameter = float(
        input("Please enter the Diameter of your pizza(inches): "))

    # Assign number of slices using conditions and print
    # assign value to variable "number_slices"
    if input_diameter >= 8.00 and input_diameter <= 24.00:

        if input_diameter >= 8.00 and input_diameter < 12.00:
            number_slices = 6
        elif input_diameter >= 12.00 and input_diameter < 14.00:
            number_slices = 8
        elif input_diameter >= 14.00 and input_diameter < 16.00:
            number_slices = 10
        elif input_diameter >= 16.00 and input_diameter < 20.00:
            number_slices = 12
        elif input_diameter >= 20.00 and input_diameter <= 24.00:
            number_slices = 16

        print("\nA", str(input_diameter), "' pizza will have",
              str(number_slices), "slices.")

        # Find area of each slice using appropriate formula and math module
        # Assign value to variable "area_slice"

        radius = input_diameter / 2

        area_slice = ((math.pi) * (radius) ** 2) / number_slices

        # Print area of each slice
        print("\nArea of each slice", str(round(area_slice, 2)), "sq. inches.")

        # Prompt the user to press ENTER to exit
        input("\nPress ENTER to exit the application...")
    else:
        # Else statement if number not within range
        print("\nThe diameter value must be 8' to 24' inclusive.")

        input("\nPress ENTER to exit the application...")
    isvalid = True

except:
    # Else statement if input is not a real number
    print("\nThe diameter value must be 8' to 24' inclusive.")

    input("\nPress ENTER to exit the application...")
    isvalid = False
