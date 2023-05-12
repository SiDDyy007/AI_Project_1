from tree_class import Node
class PuzzleNode():
    def __init__(self, data, depth, h_val, parent = None):
        self.data = data
        self.parent = parent
        self.depth = depth
        self.h_val = h_val
        self.f_val = 0
    
    def __lt__(self, other):
        return self.f_val < other.f_val

    def find_space(self):
        for row in range(len(self.data)):
            for col in range(len(self.data)):
                if self.data[row][col] == '0':
                    return row, col
                
    def generate_children(self):
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
