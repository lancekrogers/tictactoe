import sys
import math # math.factorial()
import numpy as np


def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)

# get your team & get your board
team = input()
first_row = input()
second_row = input()
third_row = input()


# print out the inputs you're getting
debug_print(team)
debug_print(first_row)
debug_print(second_row)
debug_print(third_row)



    # outputs the contents of my board
    # board == incoming board plus my coordinates

#team = input()
#first_row = input()
#second_row = input()
#third_row = input()
#almost_board = [[first_row], [second_row], [third_row]]
#board = np.array(almost_board)



def get_team():
    my_bot_team = ''
    if team == 'X':
        my_bot_team = 'X'
    else:
        my_bot_team = 'O'
    print(my_bot_team)
    return my_bot_team

def get_board():
    almost_board = first_row, second_row, third_row
    board = np.array(almost_board)
    return board

def change_stratagy():
    # logic for bot choice
    if my_bot_team not in board:
        if '_' == (board.flat[0][2]):
            print('0 2')
        elif '_' == (board.flat[0][0]):
            print('0 0')
        elif '_' == (board.flat[][])






get_team()
get_board()
