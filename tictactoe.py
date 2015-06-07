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

almost_board = [first_row], [second_row], [third_row]
board = np.array(almost_board)




def game_logic(board, team):
    # logic for bot choice
    # functions as a hierarchy of move choices
    A = (board.flat[0][2])
    B = (board.flat[0][0])
    C = (board.flat[2][0])
    D = (board.flat[2][2])
    E = (board.flat[0][1])
    F = (board.flat[2][1])
    G = (board.flat[1][0])
    H = (board.flat[1][2])
    I = (board.flat[1][1])




    if team not in board:
        # first game move

        if A and C != '_' and I == '_' or E and F != '_' and I == '_':
            print('1 1')

        elif B and D != '_' and I == '_' or G and H != '_' and I == '_':
            print('1 1')

        elif A and B != '_' and E == "_":
            print('0 1')

        elif E and I != '_' and F == '_' or C and D != '_' and F == '_':
            print('2 1')

        elif I and F != '_' and E == '_' or B and A != '_' and E == '_':
            print('0 1')

        elif G and I != '_' and H == '_':
            print('1 2')




        elif A and B != '_' and E == '_':
            print ('0 1')

        elif B and C != '_' and G == '_':
            print('1 0')

        elif C and D != '_' and F == '_':
            print('2 1')


        elif A and D != '_' and H == '_':
            print('1 2')


        elif '_' == A:
            print('0 2')

        elif '_' == B:
            print('0 0')


        elif '_' == D:
            print('2 2')


        elif '_' == C:
            print ('2 0')

        elif '_' == B:
            print('0 0')

        elif '_' == A:
            print('0 2')

        elif '_' == E:
            print('0 1')

        elif '_' == F:
            print('2 1')

        elif '_' == G:
            print('1 0')

        elif '_' == H:
            print('1 2')

        elif '_' == D:
            print('2 2')

        elif '_' == I:
            print('1 1')

        elif '_' == F:
            print('2 1')

        elif '_' == G:
            print('1 0')







def main():
    game_logic(board, team)


main()
