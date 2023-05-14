#Solution Tree Classes

'''Initialize a Node with given data and parent.'''
class Node:
    def __init__(self, data, parent=None):
        '''The data to be stored in the node.'''
        self.data = data
        '''The parent node of this node, default is None.'''
        self.parent = parent
        
'''Initialize a Tree with the given root data.'''
class Tree:
    def __init__(self, root_data):
        '''The data to be stored in the root node.'''
        self.root = Node(root_data)