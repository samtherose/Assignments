# Create and use custom functions in wordle_functions.py. Your program should include the
# functions:
# • choose_word() – Selects and returns a secret word.
# • get_guess() – Gets and validates the player’s guess.
# • evaluate_guess() – Compares the guess with the secret word and returns feedback.
# • display_guess() – Displays the guess and its feedback.
# • has_won() – Determines whether the player has guessed the word.

import random

#List of secret words. Every word is five letters long and no repeated letters.
# Got list from AI tools.
word_list = [
    "PLANT", "CRANE", "SLATE", "BRICK", "GHOST", "CHAIR", "MOUSE", "TRAIN",
    "LIGHT", "STORM", "FLAME", "GRAPE", "HOUSE", "WATER", "BREAD", "CLOUD",
    "DREAM", "EARTH", "FIGHT", "GLOVE", "HEART", "HORSE", "JUICE", "KNIFE",
    "LEMON", "MONEY", "NIGHT", "OCEAN", "PIANO", "QUEST", "ROAST", "SHIRT",
    "SMILE", "SNAKE", "SPORT", "STONE", "TABLE", "TIGER", "TRUCK", "UNCLE",
    "WORLD", "YOUTH", "BEACH", "BLACK", "BRAIN", "BROWN", "CANDY", "CHEST",
    "DANCE", "DRINK", "FAITH", "FIELD", "FLOUR", "FRUIT", "GRAND", "HONEY",
    "LUNCH", "MAGIC", "MOVIE", "NORTH", "PAINT", "PHONE", "PLATE", "POINT",
    "PRIZE", "QUIET", "RADIO", "SAINT", "SHARK", "SHELF", "SOUTH", "SPACE",
    "SUGAR", "THINK", "TOWEL", "WHALE", "WRONG", "ZEBRA"
]

def choose_word():
    # Picks a random word from the word_list and returns it.
    return random.choice(word_list)

def get_guess(previous_guesses):
    # Gathers input guess and validates it.
    while True:
        guess = input("Enter a 5 letter word: ").upper()

        if len(guess) != 5:
            print("Invalid input. Please enter a 5 letter word.")
        elif not guess.isalpha(): 
            #.isalpha() checks if all characters are alphabetic
            print("Invalid input. Please enter only letters.")
        elif guess in previous_guesses:
            print("You have already guessed that word. Try again.")
        else:
            return guess

def return_guess(guess, secret_word):
    # Compares the guess with the secret word and returns feedback.
    # G = Correct letter in correct position
    # Y = Correct letter in wrong position
    # - = Letter not in the word

    # Start a feedback assuming all letters are incorrect
    feedback = ""

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback += "G"  # Correct letter in correct position
        elif guess[i] in secret_word:
            feedback += "Y"  # Correct letter in wrong position
        else:
            feedback += "-"  # Letter not in the word
    return feedback

def display_guess(guess, feedback):
    # Displays the guess and its feedback.
    # " ".join() puts a space between each character so the letters
    # and symbols line up, e.g. "TRUST" becomes "T R U S T".
    # It only changes what is printed, not the guess or feedback variables.
    # Both labels are 10 characters long so the two lines start in the same column.
    print("Guess:    " + " ".join(guess))
    print("Feedback: " + " ".join(feedback))
    print()  # Print a blank line for better readability

def won_game(feedback):
    # Returns true if all letters in feeback is "G".
    return feedback == "GGGGG"
