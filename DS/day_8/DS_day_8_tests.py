from DS_day_8 import AVLTree

def test_insert():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    assert tree.root.key == 20
    print("Passed test_insert")

def test_LL():
    tree = AVLTree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)
    assert tree.root.key == 20
    print("Passed test_LL")

def test_RR():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    assert tree.root.key == 20
    print("Passed test_RR")

def test_LR():
    tree = AVLTree()
    tree.insert(30)
    tree.insert(10)
    tree.insert(20)
    assert tree.root.key == 20
    print("Passed test_LR")

def test_RL():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(30)
    tree.insert(20)
    assert tree.root.key == 20
    print("Passed test_RL")

def test_height():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    assert tree.height() == 2
    print("Passed test_height")

def test_is_balanced():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    assert tree.is_balanced() == True
    print("Passed test_is_balanced")

def run_all_tests():
    test_insert()
    test_LL()
    test_RR()
    test_LR()
    test_RL()
    test_height()
    test_is_balanced()

    print("Passed all tests!!!")

run_all_tests()
