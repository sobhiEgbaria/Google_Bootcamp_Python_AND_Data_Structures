class Node:
    def __init__(self, key, height=1):
        """Initializes a new node with the given key and height."""
        pass


# get the BinarySearchTree class from last lecture.
class AVLTree(BinarySearchTree):

    def LL(self, node):
        """Performs a left rotation about a node."""
        pass

    def RR(self, node):
        """Performs a right rotation about a node."""
        pass

    def LR(self, node):
        """Performs a left-right rotation about a node."""
        pass

    def RL(self, node):
        """Performs a right-left rotation about a node."""
        pass

    def insert(self, key):
        """Inserts a key into the AVL tree, maintaining its balance."""
        pass

    def _insert(self, node, key):
        """Helper method for insert. Inserts a key into the subtree rooted at node."""
        pass

    def get_balance(self, node):
        """Returns the balance factor of a node."""
        pass

    def height(self, node=None):
        """
        Returns the height of the AVL tree or the height of a specified node.
        If node is None, it should return the height of the whole tree.
        """
        pass

    def is_balanced(self, node=None):
        """
        Checks if the AVL tree or a specified node is balanced.
        If node is None, it checks the balance of the whole tree.
        """
        pass
