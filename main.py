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
        self.q_nodes = 0
        self.expanded_nodes = 0
    
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
        Accepts the puzzle input from the user row by row and returns it as a matrix.

        :Returns -> The input puzzle matrix.
        """
        # Initialize an empty list for the puzzle matrix
        puzzle = []

        # Accept each row of the puzzle input from the user
        for i in range(3):
            row = input(f"Please enter {i+1}st row of the puzzle: ").split(" ")
            puzzle.append(row)

        return puzzle


    #INPUT FUNCTIONS
    def choose_heuristic(self):
        print("Choose the heuristic function:")
        print("1. Uniform Cost Search")
        print("2. A* with the Misplaced Tile heuristic")
        print("3. A* with the Manhattan distance heuristic")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            self.heuristic = "uniform"
        elif choice == 2:
            self.heuristic = "misplaced_tile"
        elif choice == 3:
            self.heuristic = "manhattan"
        else:
            raise ValueError("Invalid choice")

    def h(self, start, goal):
            if self.heuristic == "manhattan":
                return self.manhattan_distance(start.data, goal)
            elif self.heuristic == "misplaced_tile":
                return self.misplaced_tile(start.data, goal)
            elif self.heuristic == "uniform":
                return 0
            else:
                raise ValueError("Invalid heuristic")

    def goal_test(self, start, goal):
            for row in range(len(start)):
                for col in range(len(start)):
                    if start[row][col] != goal[row][col]:
                        return False
            return True

    def manhattan_distance(self, start, goal):
            distance = 0
            for num in range(1, self.size * self.size):
                start_x, start_y = self.find_value(start, str(num))
                goal_x, goal_y = self.find_value(goal, str(num))
                distance += abs(start_x - goal_x) + abs(start_y - goal_y)
            return distance

    def misplaced_tile(self, start, goal):
        misplaced_count = 0
        for num in range(1, self.size * self.size):
            start_x, start_y = self.find_value(start, str(num))
            goal_x, goal_y = self.find_value(goal, str(num))
            if (start_x, start_y) != (goal_x, goal_y):
                misplaced_count += 1
        return misplaced_count


    def find_value(self, matrix, value):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == value:
                    return row, col
    
    def initialize_open_list(self, start_matrix, goal_matrix):
        """Initialize the open list with the start node."""
        start_node = PuzzleNode(start_matrix, 0, 0)
        start_node.h_val = self.h(start_node, goal_matrix)
        start_node.f_val = start_node.h_val + start_node.depth
        heapq.heappush(self.open_list, (start_node.f_val, start_node))

    def driver(self):
        self.choose_heuristic()
        print("Enter the start state matrix:")
        # start_matrix = self.input_puzzle()
        start_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']] #Depth 0
        start_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '0', '8']] #Depth 1
        start_matrix = [['1', '2', '3'], ['4', '5', '6'], ['0', '7', '8']] #Depth 2
        start_matrix = [['1', '2', '3'], ['0', '5', '6'], ['4', '7', '8']] # Depth 3
        start_matrix = [['1', '2', '3'], ['5', '0', '6'], ['4', '7', '8']] #Depth 4
        start_matrix = [['1', '2', '3'], ['5', '6', '0'], ['4', '7', '8']] #Depth 5
        start_matrix = [['1', '2', '3'], ['5', '6', '8'], ['4', '7', '0']] #Depth 6
        start_matrix = [['0', '1', '2'], ['5', '6', '3'], ['4', '7', '8']] #Depth 8
        start_matrix = [['1', '3', '6'], ['5', '0', '7'], ['4', '8', '2']] #Depth 12
        start_matrix = [['1', '6', '7'], ['5', '0', '3'], ['4', '8', '2']] #Depth 16
        start_matrix = [['7', '1', '2'], ['4', '8', '5'], ['6', '3', '0']] #Depth 20
        start_matrix = [['0', '7', '2'], ['4', '6', '1'], ['3', '5', '8']] #Depth 24
        # start_matrix = [['8', '6', '7'], ['2', '5', '4'], ['3', '0', '1']] #Depth 31



        goal_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
        
        self.initialize_open_list(start_matrix, goal_matrix)
        time = 0
        while self.open_list:
            time += 1
            self.expanded_nodes += 1            
            current_cost, current_node = heapq.heappop(self.open_list)
            print("Current g(n) =",current_node.depth, "and h(n) = ",current_node.h_val)
            print("Total f(n) for this state:",current_cost)
            for row in current_node.data:
                print(" ".join(row))

            if self.goal_test(current_node.data, goal_matrix):                
                print("\nGoal reached!")
                print("Max Nodes in q:",self.q_nodes,"Nodes Exapnded:",self.expanded_nodes)
                print("Time = ",time)
                break
            print("Expanding this Node ...")
            for child in current_node.generate_children():
                time += 1
                child_tuple = tuple(map(tuple, child.data))
                if child_tuple not in self.visited:                    
                    child.h_val = self.h(child, goal_matrix)
                    child.f_val = child.h_val + child.depth
                    heapq.heappush(self.open_list, (child.f_val, child))
            self.q_nodes = max(self.q_nodes, len(self.open_list))
            
        if not self.open_list:
            print("Failed to find a solution.")
PuzzleSolver(3).driver()
# s.driver()

