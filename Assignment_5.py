# Assignment 5: Rock Paper Scissors Game
# Samuel Rose
# IS 303
# Creat a Python Game of Rock Paper Scissors.

import random
choices = ["rock", "paper", "scissors"]

# functions
# player choice function to determine if the choice if valid
def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in choices:
        print(f"Sorry {choice} is not a valid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

# function to determine the winner of the round
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "loss"


# start game and main program
print("Welcome to Rock Paper Scissors!")

rounds = int(input("How many rounds would you like to play? "))
while rounds % 2 == 0:
    print("Please enter an odd number of rounds.")
    rounds = int(input("How many rounds would you like to play? "))

# Start counters for wins
player_wins = 0
computer_wins = 0

# play until one player wins the majority of rounds ties dont count.
while player_wins + computer_wins < rounds:
    player = get_player_choice()
    computer = random.choice(choices)
    print(f"The Computer chose: {computer}")

# determine winner and update counters
    result = determine_winner(player, computer)
    if result == "win":
        print(f"You win!")
        player_wins += 1
    elif result == "loss":
        print(f"You lose!")
        computer_wins += 1
    else:
        print("You tied, Play Again!")

# display final results

print("===============================")
print(f"Score -- You: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print("You Win!!!")
else:
    print("The Computer Wins! :( ")
print("Thanks for Playing!")