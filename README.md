# AI_Project_1
#CS 205 - Project 1 ( N - Puzzle )

#N Puzzle Solver
This is a Python implementation of an N Puzzle Solver, as part of the CS 205 Artificial Intelligence course in the Spring of 2023.

##What is an N Puzzle?
An N Puzzle is a popular puzzle game, also known as the sliding puzzle, where a player has to slide numbered tiles on a board to arrange them in a particular order. The most popular form of N Puzzle is the 8 Puzzle, which has 9 tiles arranged in a 3x3 grid, and the player has to slide the tiles to arrange them in numerical order.

##Project Overview
The goal of this project is to implement an efficient algorithm for solving the N Puzzle, given an initial state of the board and a desired final state. The solver will be implemented in Python, and we will be using a combination of search algorithms and heuristics to efficiently find a solution.

Our approach will be to use informed search algorithms such as A* search, along with heuristics like the Manhattan distance and linear conflict, to estimate the distance between a given state and the final state, and find the optimal path to reach the final state.

We will be testing our implementation on a variety of different N Puzzle instances, and comparing the performance of our algorithm with other existing solvers.

##Implementation Details
We will be implementing the N Puzzle Solver in Python, using object-oriented programming principles. The code will be organized into different modules, including the state representation module, the search algorithms module, and the heuristic functions module.

We will be using Python's built-in heapq module for implementing the priority queue used in the A* search algorithm. We will also be using Python's time module to measure the execution time of our algorithm.

##How to Use
To use the N Puzzle Solver, simply run the main.py file with the desired initial and final states of the puzzle. The initial and final states should be provided as strings, where the tiles are represented by numbers and the blank space is represented by a 0.

##Conclusion
This N Puzzle Solver project will be an interesting and challenging task for us, and will give us an opportunity to implement and experiment with various search algorithms and heuristics. We hope to gain a better understanding of how these algorithms work and how to optimize them for solving different types of problems.
