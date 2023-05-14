from tree_class import Node
'''PuzzleNode class, inheriting from Node class, 
representing a node in the solution tree for the N-puzzle problem'''
class PuzzleNode():
    '''Initialize a PuzzleNode with given data, level, f_val, and parent.'''
    '''
    :Parameter -> data: The data to be stored in the node (puzzle state).
    :Parameter -> parent: The parent node of this node, default is None.
    :Parameter -> depth: The depth of the node in the solution tree.
    :Parameter -> h_val: The total heuristic function value of the node.
    :Parameter -> f_val: The sum of heuristic function and depth i.e. f(n) .    
    """
    '''
    def __init__(self, data, depth, h_val, parent = None):
        self.data = data
        self.parent = parent
        self.depth = depth
        self.h_val = h_val
        self.f_val = 0
    
    def __lt__(self, other):
        return self.f_val < other.f_val

    def find_space(self):
        """
        Find the position of the blank space ('0') in the matrix.
        :Parameter -> value: The value to be searched in the matrix.
        :return    -> The row and column index of the value in the matrix.
        """
        for row in range(len(self.data)):
            for col in range(len(self.data)):
                if self.data[row][col] == '0':
                    return row, col
                
    def generate_children(self):
        '''Generate next states by moving the blank space in the four possible directions 
        (up, down, left, right)
        :return -> A list of child nodes representing the next states.'''
        n = len(self.data)
        blank_row, blank_col = self.find_space()
        possible_moves = [
            (blank_row, blank_col - 1),
            (blank_row, blank_col + 1),
            (blank_row - 1, blank_col),
            (blank_row + 1, blank_col)
        ]
        children = []
        
        for row, col in possible_moves:
            if 0 <= row < n and 0 <= col < n:
                # Create a new matrix with the blank space moved to the new position
                new_matrix = [row.copy() for row in self.data]
                new_matrix[blank_row][blank_col], new_matrix[row][col] = new_matrix[row][col], new_matrix[blank_row][blank_col]
                child = PuzzleNode(new_matrix, self.depth + 1, 0, parent = self)
                children.append(child)
                
        return children
