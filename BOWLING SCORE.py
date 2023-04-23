# ******************************************************************************

# Author:           @eddie304050
# Program name:     Bowling Scores (Arrays)
# Date:             March 8th, 2022
# Description:      Taking game scores from user input to display highest, lowest and average scores.

# ******************************************************************************


# Importing os module
import os

# Importing mean from statistics module
from statistics import mean

# Declaring list, variables & constants
score_list = []
flag = 1
UPPERBOUND_INDEX = 6
LOWER_LIMIT = 0
UPPER_LIMIT = 300
index = 0
LOWER_GAME = 1
UPPER_GAME = 7


# INPUT
while True:
    if flag == 0:
        break

    # Clears the terminal
    os.system('cls')

    # User-defined function to check validity of users input
    def score_valid(score):

        while len(score_list) <= UPPERBOUND_INDEX:
            # checks if user input is numeric
            if score.isnumeric() == True:
                # checks if user input is 0 to 300 inclusive.
                if int(score) >= LOWER_LIMIT and int(score) <= UPPER_LIMIT:
                    score_list.append(int(score))
                    break
                # checks if user input is not in given range
                elif int(score) < LOWER_LIMIT or int(score) > UPPER_LIMIT:
                    score = input(
                        "Score must be 0 to 300 inclusive. Try Again: ")
                    continue
            # checks if user input is decimal form
            elif score.isdecimal() == True:
                score = input(
                    "Score must be numeric, whole number. No decimals. Try Again: ")
                continue
            else:
                score = input(
                    "Score must be numeric, whole number. No decimals. Try Again: ")
                continue

    # Prompts User input for game 1
    score = input("Please enter score for Game 1: ")
    score_valid(score)

    # Prompts User input for game 2
    score = input("Please enter score for Game 2: ")
    score_valid(score)

    # Prompts User input for game 3
    score = input("Please enter score for Game 3: ")
    score_valid(score)

    # Prompts User input for game 4
    score = input("Please enter score for Game 4: ")
    score_valid(score)

    # Prompts User input for game 5
    score = input("Please enter score for Game 5: ")
    score_valid(score)

    # Prompts User input for game 6
    score = input("Please enter score for Game 6: ")
    score_valid(score)

    # Clears the terminal
    os.system('cls')

# OUTPUT
    print("*********************************************************************************************")
    # Displays all Game scores
    while index < UPPERBOUND_INDEX:
        for game_score in range(LOWER_GAME, UPPER_GAME):
            print("Game ", game_score, ':', score_list[index], end="\t")
            index += 1
        break
    print('\t')
    print("*********************************************************************************************")

# PROCESS
    print('\t')
    # Displays average score from score list
    print("Average score: ", round(mean(score_list), 0))
    print("\t")
    # Displays highest score from score list
    print("Highest score: ", max(score_list))
    print('\t')
    # Displays lowest score from score list
    print("Lowest score : ", min(score_list))

    print("\t")
    # Asks the user if they want to process another list.
    b = input('''Would you like to process another set of bowling scores?
            
Please enter Y to continue or N to exit: ''')

    if b.lower().strip() == 'y':
        # clears the value in list.
        score_list.clear()
        flag = 1

    elif b.lower().strip() == 'n':
        # clears the value in list.
        score_list.clear()
        flag = 0

    else:
        # clears the values in list.
        score_list.clear()
        flag = 0
