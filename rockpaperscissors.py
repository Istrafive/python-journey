import getpass # Allows player 1 and player 2's inputs to be hidden from eachother
from random import choice # Allows the AI to pick randomly pick rock paper or scissors

# ANSI escape code for the different colors
colors = {
    'red': '\033[91m',
    'end': '\033[0m',
    'green': '\033[92m'
    }

# A list containing the playable options
playables = [
    'rock',
    'paper',
    'scissors']

# The function that creates the logic of the game and returns the winner
def is_win(arg:str, arg2:str) -> str:
    if arg=='rock' and arg2=='scissors':
        return arg
    if arg=='rock' and arg2=='paper':
        return arg2
    if arg=='scissors' and arg2=='rock':
        return arg2
    if arg=='scissors' and arg2=='paper':
        return arg
    if arg=='paper' and arg2=='rock':
        return arg
    if arg=='paper' and arg2=='scissors':
        return arg2
    return 'draw'

while True:
    # Determines if the user wishes to play with another player or an 'AI'        
    play_choice = input("Enter '1' to play with an AI or enter '2' to play with another player: ")
    
    # If the user input is invalid, it keeps on asking the user to select '1' or '2'
    if play_choice!='1' and play_choice!='2':
        print(
            f"{colors['red']}You must select either '1' or '2' to play the game{colors['end']}"
            )
        continue
    else:
        break

# Checks if the user wishes to play with an 'AI'
if play_choice=='1':
    player1counter=0 # The amount of times the player has won
    AIcounter=0 # The amount of times the AI has won
    while True:
        print() # prints an empty line to avoid jumbled up lines
        player_choice = input("Choose either rock, paper or scissors: ").lower()
        print()

        # Checks if the user input is a playable option
        if player_choice not in playables:
            print(f"{colors['red']}What you have entered is not a valid choice, try again {colors['end']}")
            continue
        
        # Randomly selects a playable option from the list of playable options
        AI_choice = choice(playables)

        # Checks if the player won
        if is_win(player_choice, AI_choice)==player_choice:
            print(f"{colors['green']}Player 1 has won!{colors['end']}")
            player1counter+=1

        # Checks if the 'AI' won
        elif is_win(player_choice, AI_choice)==AI_choice:
            print(f"{colors['green']}The AI has won!{colors['end']}")
            AIcounter+=1
        else:
            print("Game ended in a draw do-over commencing...")
            continue

        print()
        print(f"The player has {player1counter} wins")
        print(f"The AI has {AIcounter} wins")
        print()

        while True:
            # Asks the user if he wishes to continue playing.
            continue_play=input(
                "Do you wish to continue playing? (if yes enter 'Y' if no enter 'N'): "
                ).upper()
            
            # Checks if the user input is valid
            if continue_play!='N' and continue_play!='Y':
                print(f"{colors['red']}What you have entered is not valid, enter 'Y' or 'N'{colors['end']}")
                continue
            else:
                break

        # Checks if the user wishes to continue playing or not    
        if continue_play=='Y':
            print("Continuing game...")
            continue
        else:
            print("Ending game...")
            break

# Checks if the user wishes to play with another player
if play_choice=='2':
    player1counter=0
    player2counter=0
    while True:
        print()

        # Another way of using input, except getpass allows the user input to be hidden from terminal
        # Thereby preventing the other player to cheat
        player1_choice = getpass.getpass("(Player 1) Choose either rock, paper or scissors: ").lower()
        print()
        
        # Checks if the user input is in the list of playable options
        if player1_choice not in playables:
            print(
                f"{colors['red']}What you have entered is not a valid choice, try again {colors['end']}"
                )
            continue

        while True:
            player2_choice = getpass.getpass("(Player 2) Choose either rock, paper or scissors: ").lower()
            if player2_choice not in playables:
                print(
                    f"{colors['red']}What you have entered is not a valid choice, try again {colors['end']}"
                    )
                continue
            else:
                break

        if is_win(player1_choice, player2_choice)==player1_choice:
            print(f"{colors['green']}Player 1 has won!{colors['end']}")
            player1counter+=1

        elif is_win(player1_choice, player2_choice)==player2_choice:
            print(f"{colors['green']}Player 2 has won!{colors['end']}")
            player2counter+=1

        else:
            print("Game ended in a draw commencing do-over...")
            continue

        print()
        print(f"Player 1 has {player1counter} wins")
        print(f"Player 2 has {player2counter} wins")
        print()

        while True:
            continue_play=input(
                "Do you wish to continue playing? (if yes enter 'Y' if no enter 'N'): "
                ).upper()
            
            if continue_play!='N' and continue_play!='Y':
                print(f"{colors['red']}What you have entered is not valid, enter 'Y' or 'N'{colors['end']}")
                continue
            else:
                break
            
        if continue_play=='Y':
            print("Continuing game...")
            continue
        else:
            print("Ending game...")
            break