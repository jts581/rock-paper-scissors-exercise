# game.py

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")

#print(user_choice)
print("User choice:", user_choice)

# validate the input such that only if it is one of the expected values
#... will we continue with the rest of the program
#... otherwise we'll stop the program before it tries to do anything else
#... and we'll ask the user to run the program again

if (user_choice == "rock") or (user_choice=="paper") or (user_choice=="scissors"):
    print("VALID, KEEP GOING")
else: 
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN")
    exit()

print("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN")