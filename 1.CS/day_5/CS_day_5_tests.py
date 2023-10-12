import sys
import io
from CS_day_5 import *


def test_create_student_dict():
    assert create_student_dict() == {
        "name": "John",
        "age": 20,
        "major": "Computer Science",
        "grades": [85, 90, 92, 88],
    }


def test_names_to_lengths():
    assert names_to_lengths(["Alice", "Bob", "Charlie"]) == {
        "Alice": 5,
        "Bob": 3,
        "Charlie": 7,
    }


def test_count_elements():
    assert count_elements([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}


def test_create_phonebook():
    assert create_phonebook(["Alice", "Bob"], ["123", "456"]) == {
        "Alice": "123",
        "Bob": "456",
    }


def test_calculate_averages():
    students = [
        {"name": "Alice", "grades": [85, 90, 92, 88]},
        {"name": "Bob", "grades": [80, 85, 89, 90]},
    ]
    assert calculate_averages(students) == {"Alice": 88.75, "Bob": 86.0}


def test_merge_dicts():
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}


def test_words_to_lengths():
    assert words_to_lengths(["apple", "banana", "cherry"]) == {
        "apple": 5,
        "banana": 6,
        "cherry": 6,
    }


def test_most_frequent():
    assert most_frequent([1, 2, 2, 3, 3, 3]) == 3


def test_search_product():
    products = [
        {"name": "apple", "price": 1.0},
        {"name": "banana", "price": 0.5},
        {"name": "cherry", "price": 0.75},
    ]
    assert search_product(products, "banana") == 0.5


def test_dict_to_tuples():
    assert dict_to_tuples({"a": 1, "b": 2, "c": 3}) == [("a", 1), ("b", 2), ("c", 3)]


def run_all_tests():
    # test_create_student_dict()
    # print("Passed test_create_student_dict")

    # test_names_to_lengths()
    # print("Passed test_names_to_lengths")

    # test_count_elements()
    # print("Passed test_count_elements")

    # test_create_phonebook()
    # print("Passed test_create_phonebook")

    # test_calculate_averages()
    # print("Passed test_calculate_averages")

    # test_merge_dicts()
    # print("Passed test_merge_dicts")

    # test_words_to_lengths()
    # print("Passed test_words_to_lengths")

    # test_most_frequent()
    # print("Passed test_most_frequent")

    # test_search_product()
    # print("Passed test_search_product")

    # test_dict_to_tuples()
    # print("Passed test_dict_to_tuples")

    # print("Passed all tests!!!")


run_all_tests()
