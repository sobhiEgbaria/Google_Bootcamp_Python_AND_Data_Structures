import io
import sys
from CS_day_7 import *


def test_factorial():
    assert factorial(5) == 120


def test_fibonacci():
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]


def test_sum_list():
    assert sum_list([1, 2, 3, 4, 5]) == 15


def test_max_element():
    assert max_element([1, 2, 3, 4, 5]) == 5


def test_power():
    assert power(2, 3) == 8


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_is_palindrome():
    assert is_palindrome("radar") == True


def test_gcd():
    assert gcd(48, 18) == 6


def test_tower_of_hanoi():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    tower_of_hanoi(3, "A", "B", "C")
    sys.stdout = sys.__stdout__
    assert (
        "Move disk from A to B\nMove disk from A to C\nMove disk from B to C\nMove disk from A to B\nMove disk from C to A\nMove disk from C to B\nMove disk from A to B\n"
        == capturedOutput.getvalue()
    )


def test_permutations():
    assert set(permutations("abc")) == set(["abc", "acb", "bac", "bca", "cab", "cba"])


def run_tests():
    test_factorial()
    print("Passed test_factorial")

    # test_fibonacci()
    # print("Passed test_fibonacci")

    # test_sum_list()
    # print("Passed test_sum_list")

    # test_max_element()
    # print("Passed test_max_element")

    # test_power()
    # print("Passed test_power")

    # test_reverse_string()
    # print("Passed test_reverse_string")

    # test_is_palindrome()
    # print("Passed test_is_palindrome")

    # test_gcd()
    # print("Passed test_gcd")

    # test_tower_of_hanoi()
    # print("Passed test_tower_of_hanoi")

    # test_permutations()
    # print("Passed test_permutations")

    # print("Passed all tests")


run_tests()
