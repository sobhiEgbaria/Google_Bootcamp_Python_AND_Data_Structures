class BinNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(root: BinNode):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


bt = BinNode(1)
bt.left = BinNode(2)
bt.right = BinNode(3)
print(height(bt))


def count_nodes(root: BinNode):
    if root is None:
        return 0

    left = count_nodes(root.left)
    right = count_nodes(root.right)

    return left + right + 1


bt = BinNode(1)
bt.left = BinNode(2)
bt.right = BinNode(3)
print(count_nodes(bt))


def min_depth(root: BinNode):
    if root is None:
        return 0
    return min(min_depth(root.left), min_depth(root.right)) + 1


bt = BinNode(1)
bt.left = BinNode(2)
bt.right = BinNode(3)
print(min_depth(bt))


def convert_array_to_binary_tree(arr):
    if arr is None:
        return None
    root = BinNode(arr[0], BinNode(arr[1]), BinNode(arr[2]))

    for i in range(1, len(arr)):
        if (2 * i + 1) > len(arr) - 1:
            break
        elif (2 * i + 2) > len(arr) - 1:
            BinNode(arr[i], BinNode(arr[2 * i + 1]))
            break
        BinNode(arr[i], BinNode(arr[2 * i + 1]), BinNode(arr[2 * i + 2]))

    return root


print(convert_array_to_binary_tree([1, 2, 3]))

# def is_full_binary_tree(root: BinNode):
#     """Checks if a binary tree is a full binary tree"""


# def is_almost_complete_binary_tree(root: BinNode):
#     """Checks if a binary tree is an almost-complete binary tree"""


# def mirror_tree(root: BinNode):
#     """Mirrors a binary tree by swapping all right and left children of all nodes"""


# def are_identical(root1: BinNode, root2: BinNode):
#     """Checks if two binary trees are identical (same structure, same node values)."""


# def max_path_sum(root: BinNode):
#     """Finds the maximum path sum in a binary tree"""


# def lowest_common_ancestor(root: BinNode, p, q):
#     """Finds the lowest common ancestor of two nodes in a binary tree"""


# def is_valid_binary_heap(root: BinNode):
#     """Checks whether a given binary tree is a valid binary heap"""
