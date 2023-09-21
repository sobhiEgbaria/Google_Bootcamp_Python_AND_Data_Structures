# Class that represents an interval
class Interval:
    def __init__(self, min=0, max=0):
        """
        Initializes an interval of the form [min,max].
        """
        self.min = min
        self.max = max


# Class that represents a node for a binary tree.
class Node:
    def __init__(self, data, left=None, right=None):
        """
        Initialize a tree node with left and right pointers.
        """
        self.data = data
        self.left = left
        self.right = right


# Class that represents a BST that stores intervals
class BinaryIntervalSearchTree:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.root = None

    def find_interval(self, q):
        """
        Returns true if there exists an interval in the tree which contains q
        and false otherwise.
        """
        # if self.root == None:
        #     return -1
        # find_interval(self.root.left)

        # find_interval(self.root.right)

    def insert(self, i):
        if self.root == None:
            return Node(i, i.high)

        if i.low < self.root.range.low:
            self.root.left = insert(self.root.left, i)
        else:
            self.root.right = insert(self.root.right, i)

        if self.root.max < i.high:
            self.root.max = i.high

        return self.root

    def rotate_right(self, x):
        """
        Performs a right rotation about a node x in the tree.
        """
        pass

    def rotate_left(self, x):
        """
        Performs a left rotation about a node x in the tree.
        """
        pass
