import sys
import numpy as np


def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)


# get your team & get your board
team = input()
first_row = input()
second_row = input()
third_row = input()
almost_board = [first_row], [second_row], [third_row]
board = np.array(almost_board)

# print out the inputs you're getting
debug_print(team)
debug_print(list(first_row))
debug_print(second_row)
debug_print(third_row)

debug_print(board)

debug_print((board.flat[0]))
debug_print((board.flat[0])[1])
debug_print((board.flat[0][1]))

# Outputting the coordinates of your board
import random
if random.random() > .5:
    print("0 1")
else:
    print("0 0")
