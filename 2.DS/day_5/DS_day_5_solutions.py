class BinNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(root: BinNode):
    """Computes the height of a binary tree"""
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


def count_nodes(root: BinNode):
    """Counts the number of nodes in a binary tree"""
    if root is None:
        return 0
    else:
        return count_nodes(root.left) + count_nodes(root.right) + 1


def min_depth(root: BinNode):
    """Finds the minimum depth of a leaf in a binary tree"""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return min_depth(root.right) + 1
    if root.right is None:
        return min_depth(root.left) + 1
    return min(min_depth(root.left), min_depth(root.right)) + 1


def convert_array_to_binary_tree(arr):
    """Converts an array representing an almost complete binary tree into a binary tree object"""

    def convert_to_node(index):
        if index >= len(arr) or arr[index] is None:
            return None
        node = BinNode(arr[index])
        node.left = convert_to_node(2 * index + 1)
        node.right = convert_to_node(2 * index + 2)
        return node

    return convert_to_node(0)


def is_full_binary_tree(root: BinNode):
    """Checks if a binary tree is a full binary tree"""
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)
    return False


def is_almost_complete_binary_tree(root: BinNode):
    """Checks if a binary tree is an almost-complete binary tree"""
    queue = [(root, 1)]
    idx = 0
    while idx < len(queue):
        node, serial = queue[idx]
        idx += 1
        if node:
            queue.append((node.left, 2 * serial))
            queue.append((node.right, 2 * serial + 1))
    return queue[-1][1] == len(queue)


def mirror_tree(root: BinNode):
    """Mirrors a binary tree by swapping all right and left children of all nodes"""
    if root:
        root.left, root.right = root.right, root.left
        mirror_tree(root.left)
        mirror_tree(root.right)
    return root


def are_identical(root1: BinNode, root2: BinNode):
    """Checks if two binary trees are identical"""
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.value == root2.value and
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right))


def max_path_sum(root: BinNode):
    """Finds the maximum path sum in a binary tree"""

    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        max_sum = max(max_sum, node.value + left_gain + right_gain)
        return node.value + max(left_gain, right_gain)

    max_sum = float('-inf')
    max_gain(root)
    return max_sum


def lowest_common_ancestor(root: BinNode, p, q):
    """Finds the lowest common ancestor of two nodes in a binary tree"""
    if not root:
        return None
    if root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left is not None else right


def is_valid_binary_heap(root: BinNode):
    """Checks whether a given binary tree is a valid binary heap"""
    if not is_almost_complete_binary_tree(root):
        return False

    def is_heap(node):
        if node.left:
            if node.value < node.left.value:
                return False
            if not is_heap(node.left):
                return False
        if node.right:
            if node.value < node.right.value:
                return False
            if not is_heap(node.right):
                return False
        return True

    return is_heap(root)
