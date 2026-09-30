# Samuel Rose
# Higher or Lower Game

# Create a Python game in which the computer chooses a random number 
# and the player tries to guess that number. After each valid guess, 
# the program should tell the player whether to guess higher or lower.

# Header
print("=============================")
print("Higher or Lower Game:")
print("=============================")

import random

# While user presses "y"
play_again = "y"

while play_again == "y":

    # Generate a Random number 1-100
    print("Im thinking of a Number 1-100.")
    secret_number = random.randint(1,100)

    # set guess count to 0
    guess_count = 0

    # While they Input your Guess:
    guess = int(input("What is your guess?: "))

    # Validate Number
    while guess < 1 or guess > 100:
        #   Print "Invalid Guess! Please Try Again"
        print("Invalid Guess! Please Try Again")
        guess = int(input("What is your Guess?: "))


    # Compare the Guess to the Secret Number
    while guess != secret_number:
    # Increment the Number of Guesses made
        guess_count += 1
            
        # compare to secret number
        if guess > secret_number:
            print("Lower")
        elif guess < secret_number:
            print("Higher")
        # Then ask for antoher guess
        guess = int(input("What is your Guess?: "))
    print("====================")
    print("You Guessed it!")

    # loop Ends

    guess_count += 1
    # Print the number of guesses
    print("It took you ", guess_count, "guesses!")

    # if the number of guesses <= 3
    if guess_count <= 3:
         print("You Are Amazing!!")
    
    # else if the number of guesses <= 5
    elif guess_count <= 5:
        print("Impressive!")

    # else if the number of guesses <= 7 
    elif guess_count <= 7:
        print("Good Job!")

    # else if the number of guesses <= 9
    elif guess_count <= 9:
        print("Took you a little longer but you got it.")

    # else if the number of guesses >= 10
    elif guess_count >= 10:
        print("You Need To Lock In.")

    # ask user to press "y" if they want to play agian.
    play_again = input("Would you like to play again? y/n: ")
    

# loop

print("Thanks for Playing!")