from helpers import draw_board
spots = {1 :'1', 2 :'2', 3 : '3', 4 :'4', 5 :'5', 6 :'6', 7 :'7', 8 :'8',9 :'9'}
draw_board(spots)
print("second draw: ")
playing = True
while playing:
    draw_board(spots)
    choice = input()
    if choice == 'q':
        playing = False

