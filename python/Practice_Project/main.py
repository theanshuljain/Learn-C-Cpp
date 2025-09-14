# This is how you comment in Python
# This file is being written as a Python programming basics document for my own reference.

# -----------------------------------------------------------------------------------

# Importing Libraries
# Libraries are pre-written code that anyone can use to write code faster and use better features already coded in the libraries.
import random

# -----------------------------------------------------------------------------------

# Variables
player_choice = 'rock'              # variables on the left, assigned values on the right
computer_choice = 'paper'

# -----------------------------------------------------------------------------------

# Dictionaries
# These are used to store data values in key:value pairs.
dict = {"name": "Anshul", "color": "orange"}

# -----------------------------------------------------------------------------------

# Creating Lists and Calling Methods
food = ["pizza", "carrots", "eggs"]
dinner = random.choice(food)
# In the above line, we used the "random" library imported at the start of the code, used its choice method to select today's dinner from the available food options in the list we created just before that.

# -----------------------------------------------------------------------------------

# If-Else Statements
num_1 = 10
num_2 = 34
if num_1 != num_2:
    print("The numbers are unequal.")
else:
    print("The numbers are equal.")

# -----------------------------------------------------------------------------------

# Functions
def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")          # calling the variables declared earlier
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices                  # returning the desired values from the function

def greeting():
    return "Hi!"

# Calling a function
greeting()                  # Does not give any output

# Playing with the functions
response = greeting()
print(response)             # Now it gives an output as it is now assigned to a variable

choices = get_choices()
print(choices)              # We want to print all the choices from the first function

# Functions with Arguments
def check_winner(player, computer):
    print(f"You chose {player}, and the computer chose {computer}.")
    if player == computer:
        return "The game is a draw."
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lost!"

# Call the check_winner function and play with it
winner = check_winner("rock", "paper")