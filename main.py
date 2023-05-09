#Importing the neccessary libraries
import math
import heapq
print ("Hello World")

#INPUT FUNCTIONS
def input_puzzle(self):
    """
    Accepts the puzzle input from the user and return it as a matrix.

    :Returns -> The input puzzle matrix.
    """
    # Accept the puzzle input from the user and return it as a matrix
    puzzle = [input().split(" ") for _ in range(3)]
    return puzzle