#Importing the neccessary libraries
import math
import heapq
from puzzle_node import PuzzleNode
print ("Hello World")

class PuzzleSolver:

    def __init__(self, size):
        self.size = size
        self.open_list = []
        self.visited = set()
    
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

    def f(self, start, goal):
            if self.heuristic == "manhattan":
                return self.manhattan_distance(start.data, goal)
            elif self.heuristic == "euclidean":
                return self.euclidean_distance(start.data, goal)
            elif self.heuristic == "uniform":
                return 0
            else:
                raise ValueError("Invalid heuristic")

    def equal_check(self, start, goal):
            for row in range(len(start)):
                for col in range(len(start)):
                    if start[row][col] != goal[row][col]:
                        return False
            return True

    def driver(self):
        self.choose_heuristic()
        print("Enter the start state matrix:")
        start_matrix = self.input_puzzle()
        goal_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]

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

    def find_value(self, matrix, value):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == value:
                    return row, col