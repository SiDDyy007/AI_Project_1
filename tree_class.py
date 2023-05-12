#Solution Tree Classes


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent

class Tree:
    def __init__(self, root_data):
        self.root = Node(root_data)