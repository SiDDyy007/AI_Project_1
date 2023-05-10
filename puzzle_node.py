class PuzzleNode():
    def __init__(self, data, depth, h_val):
        self.data = data
        self.depth = depth
        self.h_val = h_val
        self.g_val = 0
    
    def __lt__(self, other):
        return self.g_val < other.g_val

    def find_space(self):
        for row in range(len(self.data)):
            for col in range(len(self.data)):
                if self.data[row][col] == 0:
                    return row, col