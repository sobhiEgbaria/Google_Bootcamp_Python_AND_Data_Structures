from DS_day_5 import *


def test_height():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    assert height(bt) == 2


def test_count_nodes():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    assert count_nodes(bt) == 3


def test_min_depth():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    assert min_depth(bt) == 2


def test_convert_array_to_binary_tree():
    bt = convert_array_to_binary_tree([1, 2, 3])
    assert bt.value == 1
    assert bt.left.value == 2
    assert bt.right.value == 3


def test_is_full_binary_tree():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    assert is_full_binary_tree(bt) == True


def test_is_almost_complete_binary_tree():
    bt = BinNode(1)
    bt.left = BinNode(2)
    assert is_almost_complete_binary_tree(bt) == True


def test_mirror_tree():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    mirror_tree(bt)
    assert bt.left.value == 3
    assert bt.right.value == 2


def test_are_identical():
    bt1 = BinNode(1)
    bt1.left = BinNode(2)
    bt1.right = BinNode(3)

    bt2 = BinNode(1)
    bt2.left = BinNode(2)
    bt2.right = BinNode(3)
    assert are_identical(bt1, bt2) == True


def test_max_path_sum():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    assert max_path_sum(bt) == 6  # the path is 2->1->3


def test_lowest_common_ancestor():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    assert (
        lowest_common_ancestor(bt, bt.left, bt.right).value == 1
    )  # LCA of 2 and 3 is 1


def test_is_valid_binary_heap():
    bt = BinNode(1)
    bt.left = BinNode(2)
    bt.right = BinNode(3)
    assert (
        is_valid_binary_heap(bt) == False
    )  # Not a valid binary heap as 1 < 2 and 1 < 3


def run_all_tests():
    # test_height()
    # print("Passed test_height")

    # test_count_nodes()
    # print("Passed test_count_nodes")

    # test_min_depth()
    # print("Passed test_min_depth")

    test_convert_array_to_binary_tree()
    print("Passed test_convert_array_to_binary_tree")


#     test_is_full_binary_tree()
#     print("Passed test_is_full_binary_tree")

#     test_is_almost_complete_binary_tree()
#     print("Passed test_is_almost_complete_binary_tree")

#     test_mirror_tree()
#     print("Passed test_mirror_tree")

#     test_are_identical()
#     print("Passed test_are_identical")

#     test_max_path_sum()
#     print("Passed test_max_path_sum")

#     test_lowest_common_ancestor()
#     print("Passed test_lowest_common_ancestor")

#     test_is_valid_binary_heap()
#     print("Passed test_is_valid_binary_heap")

#     print("Passed all tests!!!")


run_all_tests()
