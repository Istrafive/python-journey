import random

def main() -> None:
    print("""
    Welcome to Malcolm's Demo Domino Code, let me explain how this works. this game can only be played with
    4 players (ONLY) and each player is randomly given a list of 7 dominoes with the format:
    (top num)|(bottom num)
    the game will locate the specific domino: 6|6 and take it from a player's hand and place it on the 
    playing board, after this happens that player who the domino has been taken from will have their turn
    skipped and the next player has to play. Like real domino, only a domino with the number can be played
    on another domino with that same number.
        """)

    # This small code is responsible for adding all the dominoes to a list and then shuffling that list
    dominoes_lst = []
    for i in range(7):
        for j in range(i, 7):
            domino = f"{i}|{j}"
            dominoes_lst.append(domino)
    random.shuffle(dominoes_lst)

    # This code makes sure that if there is a player with 4 or more doubles, the game should restart
    while True:
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
    board = []
    player_with_double_six = 0
    for n in range(len(player_hand)):
        if "6|6" in player_hand[n]:
            board.append("6|6")
            player_hand[n].remove("6|6")
            player_with_double_six = n
            break

    player_turn = (player_with_double_six + 1) % 4
    print(f"It's player {player_turn + 1}'s time to play")
    print()
    print(f"Board: {board}")

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

    # This code will check if the domino the player has decided to play is playable or not
    def is_playable(domino_play, board)->bool:
        left_end = board[0].split('|')[0]
        right_end = board[-1].split('|')[-1]
        left_play = domino_play.split('|')[0] == left_end or domino_play.split('|')[-1] == left_end
        right_play = domino_play.split('|')[0] == right_end or domino_play.split('|')[-1] == right_end
        return left_play, right_play

    while True:
        print()
        print(f"{colors['cyan']}It's player {player_turn + 1}'s time to play{colors['end']}")
        print()
        print(f"{colors['yellow']}Player {player_turn + 1}'s hand: {player_hand[player_turn]}{colors['end']}")
        print()
        
        # Check if player can play any domino
        can_play = False
        for domino in player_hand[player_turn]:
            if any(is_playable(domino, board)):
                can_play = True
                break

        if not can_play:
            print(f"{colors['red']}Player {player_turn + 1} cannot play any domino. Skipping turn.{colors['end']}")
            print()
            print(f"{colors['green']}Board: {board}{colors['end']}")
            player_turn = (player_turn + 1) % 4
            continue
        
        w_play = input(f"{colors['blue']}Select the index of the domino (starting at 1) that you wish to play: {colors['end']}")
        print()

        if not w_play.isdigit():
            print(f"{colors['magenta']}Maybe try using a number this time? (preferably a whole one){colors['end']}")
            print()
            continue
        
        w_play = int(w_play)
        if w_play < 1:
            print(f"{colors['red']}I told you the index starts at 1{colors['end']}")
            print()
            continue
        if w_play > len(player_hand[player_turn]):
            print(f"{colors['red']}Trying to play a domino you don't have?{colors['end']}")
            print()
            continue

        selected_domino = player_hand[player_turn][w_play - 1]
        left_play, right_play = is_playable(selected_domino, board)

        if not left_play and not right_play:
            print(f"{colors['red']}This domino can't be played, try again{colors['end']}")
            print()
            print(f'board: {board}')
            print()
            continue

        if left_play and right_play:
            end_choice = input(f"{colors['blue']}Select the end to play on (0 for left, -1 for right): {colors['end']}")
            if end_choice not in ['0', '-1']:
                print(f"{colors['red']}Invalid choice. Try again.{colors['end']}")
                print()
                print(f"{colors['end']}board: {board}")
                print()
                continue
            end_choice = int(end_choice)
        elif left_play:
            end_choice = 0
        else:
            end_choice = -1

        if end_choice == 0:
            if selected_domino.split('|')[-1] == board[0].split('|')[0]:
                board.insert(0, selected_domino)
            else:
                board.insert(0, f"{selected_domino.split('|')[-1]}|{selected_domino.split('|')[0]}")
        elif end_choice == -1:
            if selected_domino.split('|')[0] == board[-1].split('|')[-1]:
                board.append(selected_domino)
            else:
                board.append(f"{selected_domino.split('|')[-1]}|{selected_domino.split('|')[0]}")

        player_hand[player_turn].remove(selected_domino)
        print(f"{colors['green']}Board: {board}{colors['end']}")
        if len(player_hand[player_turn]) == 0:
            print()
            print(f"{colors['cyan']}Player {player_turn + 1} has won! Congrats{colors['end']}")
            break
        player_turn = (player_turn + 1) % 4

if __name__=='__main__':
    main()