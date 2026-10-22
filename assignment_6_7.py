# Samuel Rose
# Assignment 0607
# 
# Create Python word-guessing game inspired by Wordle.
# The computer will select a secret five-letter word. 
# The player gets six attempts to guess the word.
#  Main program will be in assignment_6_7.py.
#  functions inported from wordle_functions.py.

from wordle_function import choose_word, get_guess, return_guess, display_guess, won_game

max_attempts = 6

# Start program with wwecome and instructions with explanation of the game.
print("Welcome to Wordle!")
print("You have 6 attempts to guess the 5-letter word.")
print(" G = Correct letter in correct position")
print(" Y = Correct letter in wrong position")
print(" - = Letter not in the word")

play_again = "yes"

# Main game loop to allow player to play again.
while play_again.lower() == "yes" or play_again.lower() == "y":
    secret_word = choose_word()
    previous_guesses = [] #keep track of previous guesses
    won = False

    # take evaluate and count guesses until player wins or runs out of attempts.
    for attempt in range(1, max_attempts +1):
        print(f"Attempt {attempt} of {max_attempts}")

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = return_guess(guess, secret_word)
        display_guess(guess, feedback)

        if won_game(feedback):
            print("Congratulations! You've guessed the word!")
            won = True
            break

    # Show end results of the game and ask if player wants to play again.
    if won:
        print(f"You guessed the word '{secret_word}' in {attempt} attempts!")
    else:
        print(f"Sorry, you've used all attempts. The secret word was '{secret_word}'.")

    # Ask player if they want to play again.
    play_again = input("Do you want to play again? (yes/no): ").lower()
    print()

print("Thank you for playing Wordle!")