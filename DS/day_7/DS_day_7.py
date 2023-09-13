class Node:
    """
    A Node class for Binary Search Tree (BST).

    Attributes:
    key: An integer key for the node.
    left (Node): A reference to the left child of the node.
    right (Node): A reference to the right child of the node.
    """

    def __init__(self, key):
        """
        Inits Node with key and initializes left and right children as None.
        """
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree:
    """
    A Binary Search Tree (BST) class.

    Attributes:
    root (Node): The root node of the tree.
    """

    def insert(a, x):
        pass

    def __init__(self, root=None):
        self.root = root

    def minimum(self, cur):
        while cur.left is not None:
            cur = cur.left
        return cur


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

bst.minimum() == 20


# def maximum(self):
#     """
#     Returns the node key with the maximum key in the BST.
#     """
#     pass

# def search(self, key):
#     """
#     Searches for a node with the specified key in the BST.
#     Returns the node if found, otherwise returns None.
#     """
#     pass

# def successor(self, key):
#     """
#     Returns the node with the smallest key that is larger than the specified key.
#     """
#     pass

# def predecessor(self, key):
#     """
#     Returns the node with the largest key that is smaller than the specified key.
#     """
#     pass

# def insert(self, key):
#     """
#     Inserts a node with the provided key into the BST.
#     """
#     pass

# def delete(self, key):
#     """
#     Deletes a node with the specified key from the BST.
#     """
#     pass

# def is_bst(self):
#     """
#     Checks if the tree is a valid Binary Search Tree.
#     Returns True if it is, False otherwise.
#     """
#     pass

# def height(self):
#     """
#     Returns the height of the BST.
#     """
#     pass

# def is_balanced(self):
#     """
#     Checks if the BST is balanced, meaning the depths of any two leaf nodes differ by no more than 1.
#     Returns True if it is, False otherwise.
#     """
#     pass
