import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choices()
print (choices)

def determine_winner(player,computer):
    print(f"You choose {player} and computer choose {computer}")
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win")  
        