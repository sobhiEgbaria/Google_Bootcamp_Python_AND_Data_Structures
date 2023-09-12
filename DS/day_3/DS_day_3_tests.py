import unittest
from unittest.mock import patch
from DS_day_3 import *


def test_person_node():
    # Create a person node and test its attributes
    person = PersonNode("John Doe", 30)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.next_node == None


def test_add_and_repr():
    # Create a person list and add a person
    person_list = PersonList()
    person_list.add("John Doe", 30)
    assert repr(person_list) == "PersonNode(John Doe, 30) -> None"


def test_list_length():
    # Create a person list and add two persons
    person_list = PersonList()
    person_list.add("John Doe", 30)
    person_list.add("Jane Doe", 25)
    assert person_list.list_length() == 2


def test_copy_list():
    # Create a person list and add two persons
    person_list = PersonList()
    person_list.add("John Doe", 30)
    person_list.add("Jane Doe", 25)

    # Copy the person list and check it matches the original
    copied_list = person_list.copy_list()
    assert repr(copied_list) == repr(person_list)


def test_add_israeli_and_is_in_line():
    # Create a person list and add some persons
    person_list = PersonList()
    person_list.add("John", 25)
    person_list.add("Jane", 30)
    person_list.add("Doe", 35)

    # Mock user inputs
    user_inputs = ["John", "Alice", "Bob", "Robert", "40"]

    # Use 'patch' to replace 'input' with a lambda function that returns our mock inputs
    with patch("builtins.input", side_effect=user_inputs):
        person_list.add_israeli("Robert", 40)

    correct_node = person_list.head.next_node
    # Assert that the new person is added after the frontmost friend in the queue
    assert correct_node.name == "Robert"
    assert correct_node.age == 40

    # Assert that a person with a certain name is in the queue
    assert person_list.is_in_line("John") == True

    # Assert that a person with a certain name is not in the queue
    assert person_list.is_in_line("Alice") == False


def test_is_in_line():
    # Create a person list and add some persons
    person_list = PersonList()
    person_list.add("John", 25)
    person_list.add("Jane", 30)

    # Assert that a person with a certain name is in the queue
    assert person_list.is_in_line("John") == True

    # Assert that a person with a certain name is not in the queue
    assert person_list.is_in_line("Alice") == False


def test_contains_loop():
    # Create a person list without a loop
    person_list = PersonList()
    person_list.add("John", 25)
    person_list.add("Jane", 30)

    # Assert that the list does not contain a loop
    assert person_list.contains_loop() == False

    # Create a person list with a loop
    person_list_with_loop = PersonList()
    node1 = PersonNode("John", 25)
    node2 = PersonNode("Jane", 30)
    node3 = PersonNode("Alice", 35)
    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node1
    person_list_with_loop.head = node1

    # Assert that the list contains a loop
    assert person_list_with_loop.contains_loop() == True


def test_is_tail():
    # Create a list X
    person_list_x = PersonList()
    person_list_x.add("John", 25)
    person_list_x.add("Jane", 30)
    person_list_x.add("Alice", 35)

    # Create a list Y that is a tail of list X
    person_list_y = PersonList()
    node_y = person_list_x.head.next_node
    person_list_y.head = node_y

    # Assert that list Y is a tail of list X
    assert is_tail(person_list_x.head, person_list_y.head) == True

    # Create a list Y that is not a tail of list X
    person_list_y = PersonList()
    person_list_y.add("Alice", 35)
    person_list_y.add("Bob", 40)

    # Assert that list Y is not a tail of list X
    assert is_tail(person_list_x.head, person_list_y.head) == False


def run_all_tests():
    # Q1
    test_person_node()
    print("test test_person_node passed")

    # # Q2
    # test_add_and_repr()
    # print("test test_add_and_repr passed")

    # test_list_length()
    # print("test test_list_length passed")

    # test_copy_list()
    # print("test test_copy_list passed")

    # test_add_israeli_and_is_in_line()
    # print("Passed test_add_israeli_and_is_in_line")

    # test_is_in_line()
    # print("Passed test_is_in_line")

    # test_contains_loop()
    # print("Passed test_contains_loop")

    # test_is_tail()
    # print("Passed test_is_tail")

    # print("All tests passed!")


run_all_tests()


# from DS_day_3 import LinkedList


# def test_insert_last():
#     ll = LinkedList()
#     ll.insert_last(1)
#     assert str(ll) == "1 -> null"


# def test_insert():
#     ll = LinkedList()
#     ll.insert_last(1)
#     ll.insert_last(3)
#     ll.insert(1, 2)
#     assert str(ll) == "1 -> 2 -> 3 -> null"


# def test_remove():
#     ll = LinkedList()
#     ll.insert_last(1)
#     ll.insert_last(2)
#     removed_element = ll.remove(1)
#     assert removed_element == 2
#     assert str(ll) == "1 -> null"


# def test_reverse():
#     ll = LinkedList()
#     ll.insert_last(1)
#     ll.insert_last(2)
#     ll.insert_last(3)
#     ll.reverse()
#     assert str(ll) == "3 -> 2 -> 1 -> null"


# def run_LinkedList_tests():
#     print("Running LinkedList tests...")
#     test_insert_last()
#     print("Passed test_insert_last")

#     test_insert()
#     print("Passed test_insert")

#     test_remove()
#     print("Passed test_remove")

#     test_reverse()
#     print("Passed test_reverse")

#     print("Passed all tests!!!")


# run_LinkedList_tests()
