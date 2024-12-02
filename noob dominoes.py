import random

print("""
Welcome to my Demo Domino Code, let me explain how this works. this game can only be played with
4 players (ONLY) and each player is randomly given a list of 7 dominoes with the format:
(top num)|(bottom num)
the game will locate the specific domino: 6|6 and take it from a player's hand and place it on the 
playing board, after this happens that player who the domino has been taken from will have their turn
skipped and the next player has to play. Like real domino, only a domino with the number can be played
on another domino with that same number.
      """
)

# this small code is responsible for adding all the dominoes to a list and then shuffling that list
dominoes_lst = []
for i in range(7):
    for j in range(i, 7):
        dominoes_lst.append(f"{i}|{j}")
random.shuffle(dominoes_lst)

# this is a list for the keywords to end the game
stop = ['end', 'stop', 'finish', 'terminate', 'conclude', 'false']

# This code makes sure that if there is a player with 4 or more doubles, the game should restart
while True:
    amt_skips = 0    # Tracks the amount of times a consecutive skip has occurred
    target_doub = 4
    player_hand = [dominoes_lst[:7], dominoes_lst[7:14], dominoes_lst[14:21], dominoes_lst[21:]]
    restart = False
    for hand in player_hand:
        counter = 0
        for card in hand:
            if card[0] == card[-1]:
                counter += 1
        if counter >= target_doub:
            random.shuffle(dominoes_lst)
            restart = True
            break

    if not restart:
        break

# This code will determine the number of players and how the game will be played
board = ""
player_with_double_six = 0

for n in range(len(player_hand)):
    if "6|6" in player_hand[n]:
        board = "6|6"
        player_hand[n].remove("6|6")
        player_with_double_six = n
        break

player_turn = (player_with_double_six + 1) % 4
print()
print(f"board: {board}")
cards_played=[board]

# ANSI escape codes for colors
colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'end': '\033[0m'
}

# This code will check the domino that the player has decided to play is playable or not
# as well as how it is playable
def is_playable(domino_play, domino_on_board):
    if domino_play[0] == domino_on_board[0] and domino_play[2] == domino_on_board[2]:
        return -1
    
    elif domino_play[0] == domino_on_board[0]:
        return 1
    
    elif domino_play[0] == domino_on_board[2]:
        return 2
    
    elif domino_play[2] == domino_on_board[0]:
        return 3
    
    elif domino_play[2] == domino_on_board[2]:
        return 4
    
    return False

while True:
    print()
    print(f"{colors['cyan']}It's player {player_turn + 1}'s time to play{colors['end']}")
    print()
    print(f"{colors['yellow']}Player {player_turn + 1}'s hand: {player_hand[player_turn]}{colors['end']}")
    print()
    
    # Check if player can play any domino
    can_play = False
    for domino in player_hand[player_turn]:
        if is_playable(domino, board)!=False:
            can_play = True
            break

# If the player cannot play a domino, it automatically skips their turn
    if not can_play:
        amt_skips += 1
        print(f"{colors['red']}Player {player_turn + 1} cannot play any domino. Skipping turn.{colors['end']}")
        print()
        print(f"{colors['green']}board: {board}{colors['end']}")
        player_turn = (player_turn + 1) % 4
        continue
    else:
        amt_skips = 0
    
    w_play = input(
        f"{colors['blue']} Select the index of the domino (starting at 1) that you wish to play: (you can enter 'stop' 'end' 'terminate' 'finish' or 'false' to stop playing): {colors['end']}"
        )
    print()

    if w_play.lower() in stop:
        print("Ending game...")
        break

    if not w_play.isdigit():
        print(
            f"{colors['magenta']}Maybe try using a number this time? (preferably a whole one){colors['end']}"
            )
        print()
        print(f"board = {board}")
        continue
    
    w_play = int(w_play)
    
    if w_play < 1:
        print(
            f"{colors['red']}I told you the index starts at 1{colors['end']}"
            )
        print()
        print(f"board = {board}")
        continue

    if w_play > len(player_hand[player_turn]):
        print(
        f"{colors['red']}Trying to play a domino you don't have? you only have {len(player_hand[player_turn])} dominoes{colors['end']}"
        )
        print()
        print(f"board = {board}")
        continue
    
    if is_playable(player_hand[player_turn][w_play - 1], board) == -1:
        select_end = input(
            """Select the placement of where you want to place your domino:
            (for '2|3' 1 places it at the front and 3 places it at the back/end)
            """
        )

        if not select_end.isdigit():
            print(f"{colors['green']}Maybe try using a number this time?")
            print()
            print(f"board = {board}")
            continue
        else:
            select_end = int(select_end)
            if select_end == 2:
                print("You can't select the line that splits the numbers")
                print()
                print(f"board = {board}")
                continue

            elif select_end < 1:
                print("You can't select an index of the domino that doesn't exist")
                print()
                print(f"board = {board}")
                continue

            elif select_end > 3:
                print(f"{colors['cyan']}The domino cannot have more than an index of 2, try again")
                print()
                print(f"board = {board}")
                continue

            elif select_end == 1:
                board = f"{board[2]}|{board[2]}"

            elif select_end == 3:
                board = f"{board[0]}|{board[0]}"
                
            cards_played.append(player_hand[player_turn][w_play - 1])
            player_hand[player_turn].remove(player_hand[player_turn][w_play - 1])
            print(f"{colors['magenta']}dominoes played thus far: {cards_played}")
            print()
            print(f"{colors['green']}Board: {board}{colors['end']}")

        if len(player_hand[player_turn]) == 0:
            print()
            print(f"{colors['cyan']}Player {player_turn + 1} has won! Congrats{colors['end']}")
            break

        player_turn = (player_turn + 1) % 4

    if is_playable(player_hand[player_turn][w_play - 1], board) == 1:
        board = f"{player_hand[player_turn][w_play - 1][2]}|{board[2]}"
        cards_played.append(player_hand[player_turn][w_play - 1])
        player_hand[player_turn].remove(player_hand[player_turn][w_play - 1])
        print(f"dominoes played thus far: {cards_played}")
        print(f"{colors['green']}Board: {board}{colors['end']}")

        if len(player_hand[player_turn]) == 0:
            print()
            print(f"{colors['cyan']}Player {player_turn + 1} has won! Congrats{colors['end']}")
            break
        player_turn = (player_turn + 1) % 4

    if is_playable(player_hand[player_turn][w_play - 1], board) == 2:
        board = f"{board[0]}|{player_hand[player_turn][w_play - 1][2]}"
        cards_played.append(player_hand[player_turn][w_play - 1])
        player_hand[player_turn].remove(player_hand[player_turn][w_play - 1])
        print(f"dominoes played thus far: {cards_played}")
        print(f"{colors['green']}Board: {board}{colors['end']}")

        if len(player_hand[player_turn]) == 0:
            print()
            print(f"{colors['cyan']}Player {player_turn + 1} has won! Congrats{colors['end']}")
            break
        player_turn = (player_turn + 1) % 4

    if is_playable(player_hand[player_turn][w_play - 1], board) == 3:
        board = f"{player_hand[player_turn][w_play - 1][0]}|{board[2]}"
        cards_played.append(player_hand[player_turn][w_play - 1])
        player_hand[player_turn].remove(player_hand[player_turn][w_play - 1])
        print(f"dominoes played thus far: {cards_played}")
        print(f"{colors['green']}Board: {board}{colors['end']}")

        if len(player_hand[player_turn]) == 0:
            print()
            print(f"{colors['cyan']}Player {player_turn + 1} has won! Congrats{colors['end']}")
            break
        player_turn = (player_turn + 1) % 4

    if is_playable(player_hand[player_turn][w_play - 1], board) == 4:
        board = f"{board[0]}|{player_hand[player_turn][w_play - 1][0]}"
        cards_played.append(player_hand[player_turn][w_play - 1])
        player_hand[player_turn].remove(player_hand[player_turn][w_play - 1])
        print(f"dominoes played thus far: {cards_played}")
        print(f"{colors['green']}Board: {board}{colors['end']}")

        if len(player_hand[player_turn]) == 0:
            print()
            print(f"{colors['cyan']}Player {player_turn + 1} has won! Congrats{colors['end']}")
            break
        player_turn = (player_turn + 1) % 4

    if is_playable(player_hand[player_turn][w_play - 1], board) == False:
        print()
        print(f"{colors['red']}This domino can't be played, try again{colors['end']}")
    
    if amt_skips == 4:
        currentplayercount = 0
        otherplayercount = 0
        other2playercount = 0
        other3playercount = 0
        print()
        print("""Everyone has passed, therefore to determine the winner a count will be done
              on each player's hand and the player with the lowest count will be the winner""")
        print()
        if player_turn==0:
            for domino in player_hand[player_turn]:
                currentplayercount += domino[0] + domino[2]
            for domino in player_hand[1]:
                otherplayercount += domino[0] + domino[2]
            for domino in player_hand[2]:
                other2playercount += domino[0] + domino[2]
            for domino in player_hand[3]:
                other3playercount += domino[0] + domino[2]

            print(f"""
                  Player 1 counts {currentplayercount}
                  Player 2 counts {otherplayercount}
                  Player 3 counts {other2playercount}
                  Player 4 counts {other3playercount}""")
            print()

            winner = min(currentplayercount,otherplayercount,other2playercount,other3playercount)
            if winner == currentplayercount:
                print(f"The winner is player 1 who counts {currentplayercount}")
            elif winner == otherplayercount:
                print(f"The winner is player 2 who counts {otherplayercount}")
            elif winner == other2playercount:
                print(f"The winner is player 3 who counts {other2playercount}")
            elif winner == other3playercount:
                print(f"The winner is player 4 who counts {other3playercount}")
            break
        
        elif player_turn==1:
            for domino in player_hand[player_turn]:
                currentplayercount += domino[0] + domino[2]
            for domino in player_hand[2]:
                otherplayercount += domino[0] + domino[2]
            for domino in player_hand[3]:
                other2playercount += domino[0] + domino[2]
            for domino in player_hand[0]:
                other3playercount += domino[0] + domino[2]
            
            print(f"""
                  Player 2 counts {currentplayercount}
                  Player 3 counts {otherplayercount}
                  Player 4 counts {other2playercount}
                  Player 1 counts {other3playercount}""")
            print()

            winner = min(currentplayercount,otherplayercount,other2playercount,other3playercount)
            if winner == currentplayercount:
                print(f"The winner is player 2 who counts {currentplayercount}")
            elif winner == otherplayercount:
                print(f"The winner is player 3 who counts {otherplayercount}")
            elif winner == other2playercount:
                print(f"The winner is player 4 who counts {other2playercount}")
            elif winner == other3playercount:
                print(f"The winner is player 1 who counts {other3playercount}")
            break

        elif player_turn==2:
            for domino in player_hand[player_turn]:
                currentplayercount += domino[0] + domino[2]
            for domino in player_hand[3]:
                otherplayercount += domino[0] + domino[2]
            for domino in player_hand[0]:
                other2playercount += domino[0] + domino[2]
            for domino in player_hand[1]:
                other3playercount += domino[0] + domino[2]

            print(f"""
                  Player 3 counts {currentplayercount}
                  Player 4 counts {otherplayercount}
                  Player 1 counts {other2playercount}
                  Player 2 counts {other3playercount}""")
            print()

            winner = min(currentplayercount,otherplayercount,other2playercount,other3playercount)
            if winner == currentplayercount:
                print(f"The winner is player 3 who counts {currentplayercount}")
            elif winner == otherplayercount:
                print(f"The winner is player 4 who counts {otherplayercount}")
            elif winner == other2playercount:
                print(f"The winner is player 1 who counts {other2playercount}")
            elif winner == other3playercount:
                print(f"The winner is player 2 who counts {other3playercount}")
            break

        elif player_turn==3:
            for domino in player_hand[player_turn]:
                currentplayercount += domino[0] + domino[2]
            for domino in player_hand[0]:
                otherplayercount += domino[0] + domino[2]
            for domino in player_hand[1]:
                other2playercount += domino[0] + domino[2]
            for domino in player_hand[2]:
                other3playercount += domino[0] + domino[2]
            
            print(f"""
                  Player 4 counts {currentplayercount}
                  Player 1 counts {otherplayercount}
                  Player 2 counts {other2playercount}
                  Player 3 counts {other3playercount}""")
            print()

            winner = min(currentplayercount,otherplayercount,other2playercount,other3playercount)
            if winner == currentplayercount:
                print(f"The winner is player 4 who counts {currentplayercount}")
            elif winner == otherplayercount:
                print(f"The winner is player 1 who counts {otherplayercount}")
            elif winner == other2playercount:
                print(f"The winner is player 2 who counts {other2playercount}")
            elif winner == other3playercount:
                print(f"The winner is player 3 who counts {other3playercount}")
            break

        
