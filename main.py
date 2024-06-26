from helpers import draw_board, check_turn, check_for_win

import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
turn = 0
prev_turn = -1
while playing:
    draw_board(spots)
    # clear screen if windows 'cls' if unix 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # get input from user

    if prev_turn == turn:  # doubt
        print("your spot is already taken")
    prev_turn = turn
    print(f"player {str((turn % 2) + 1)} 's turn: Pick your spot or press q to quit")

    choice = input()

    # to stop
    if choice == 'q':
        playing = False
    # to check number is in the board in  spots
    elif str.isdigit(choice) and int(choice) in spots:
        # to check the spot already taken
        if not spots[int(choice)] in {"x", "o"}:
            turn += 1

            spots[int(choice)] = check_turn(turn)  # doubt
    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8:
        playing = False
# os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
if complete:
    if check_turn(turn) == 'x':
        print("player 1 wins!")
    else:
        print("player 2 wins!")
else:
    print("No winner")
print("Thanks for playing!")
