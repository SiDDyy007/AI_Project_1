#Importing the neccessary libraries
import math
import heapq
from puzzle_node import PuzzleNode
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

#INPUT FUNCTIONS
def choose_heuristic(self):
    print("Choose the heuristic function:")
    print("1. Uniform Cost Search")
    print("2. A* with the Misplaced Tile heuristic (Manhattan distance)")
    print("3. A* with the Euclidean distance heuristic")
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        self.heuristic = "uniform"
    elif choice == 2:
        self.heuristic = "manhattan"
    elif choice == 3:
        self.heuristic = "euclidean"
    else:
        raise ValueError("Invalid choice")

def driver(self):
    self.choose_heuristic()
    print("Enter the start state matrix:")

def manhattan_distance(self, start, goal):
        distance = 0
        for num in range(1, self.size * self.size):
            start_x, start_y = self.find_value(start, str(num))
            goal_x, goal_y = self.find_value(goal, str(num))
            distance += abs(start_x - goal_x) + abs(start_y - goal_y)
        return distance

def euclidean_distance(self, start, goal):
        distance = 0
        for num in range(1, self.size * self.size):
            start_x, start_y = self.find_value(start, str(num))
            goal_x, goal_y = self.find_value(goal, str(num))
            distance += math.sqrt((start_x - goal_x) ** 2 + (start_y - goal_y) ** 2)
        return distance
