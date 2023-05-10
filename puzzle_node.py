class PuzzleNode():
    def __init__(self, data, depth, h_val):
        self.data = data
        self.depth = depth
        self.h_val = h_val
        self.g_val = 0