from DS_day_7 import *


def test_insert_and_search():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    assert bst.search(50).key == 50
    assert bst.search(100) is None


def test_minimum_and_maximum():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    assert bst.minimum() == 20
    assert bst.maximum() == 80


def test_predecessor_and_successor():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    assert bst.predecessor(30) == 20
    assert bst.successor(30) == 40

    assert bst.predecessor(80) == 70
    assert bst.successor(80) == None


def test_delete():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # delete 20, 30, 50
    bst.delete(20)
    bst.delete(30)
    bst.delete(50)

    # delete 100, which is not in the tree
    bst.delete(100)

    assert bst.search(20) is None
    assert bst.search(30) is None
    assert bst.search(50) is None


def test_is_bst():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    assert bst.is_bst() is True

    non_bst = BinarySearchTree()
    non_bst.insert(4)
    non_bst.root.right = Node(3)
    assert non_bst.is_bst() is False


def test_height():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    assert bst.height() == 3


def test_is_balanced():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    assert bst.is_balanced() is True

    unbalanced_bst = BinarySearchTree()
    unbalanced_bst.insert(4)
    unbalanced_bst.insert(3)
    unbalanced_bst.insert(2)
    unbalanced_bst.insert(1)

    assert unbalanced_bst.is_balanced() is False


def run_all_tests():
    test_insert_and_search()
    print("Passed test_insert_and_search")

    test_minimum_and_maximum()
    print("Passed test_minimum_and_maximum")

    test_predecessor_and_successor()
    print("Passed test_predecessor_and_successor")

    test_delete()
    print("Passed test_delete")

    test_is_bst()
    print("Passed test_is_bst")

    test_height()
    print("Passed test_height")

    test_is_balanced()
    print("Passed test_is_balanced")

    print("Passed all tests!!!")


run_all_tests()
