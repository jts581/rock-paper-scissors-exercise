# game.py

import random

import os

import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME")


#print(PLAYER_NAME)

print("Welcome "+ PLAYER_NAME + ", to the game of games")

print("-----------------------------")
print("Rock, Paper, Scissors, Shoot!")
print("-----------------------------")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")

#print(user_choice)
print("-----------------------------")
print("USER CHOICE:", user_choice)

# validate the input such that only if it is one of the expected values
#... will we continue with the rest of the program
#... otherwise we'll stop the program before it tries to do anything else
#... and we'll ask the user to run the program again

if (user_choice == "rock") or (user_choice=="paper") or (user_choice=="scissors"):
    print("VALID, KEEP GOING")
else: 
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN")
    exit()
print("-----------------------------")

valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:",computer_choice)
print("-----------------------------")

# determine the winner
if user_choice == computer_choice:
    print("ITS A TIE, NO ONE WINS")
    
elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
    print("COMPUTER WINS, YOU LOSE!")

else:
    print("YOU WIN, COMPUTER LOSES!")

print("-----------------------------")
print("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN")