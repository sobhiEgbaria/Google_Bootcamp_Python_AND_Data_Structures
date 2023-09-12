import io
from CS_day_4 import *

# change it to the name of your file
import CS_day_4


# 1. Local Variable Scope
def test_calculate_factorial():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(3) == 6


# 2. Global Variable Increment
def test_increment_counter():
    global counter
    CS_day_4.counter = 0  # resetting the counter
    increment_counter()
    assert CS_day_4.counter == 1
    increment_counter()
    assert CS_day_4.counter == 2


# 3. Global and Local Variables Interaction
def test_check_palindrome():
    global vowel_count
    CS_day_4.vowel_count = 0  # resetting the count
    assert check_palindrome("madam") == True
    assert check_palindrome("apple") == False
    assert CS_day_4.vowel_count == 2


# 4. Sum of Global and Local Variables
def test_calculate_sum():
    assert calculate_sum(10) == 60
    assert calculate_sum(0) == 50


# 5. Global Constants
def test_calculate_circle_area():
    assert abs(calculate_circle_area(1.0) - 3.14159) < 0.00001
    assert abs(calculate_circle_area(2.0) - 12.56636) < 0.00001


# 6. Symmetric Difference of Multiple Sets
def test_find_symmetric_difference():
    assert find_symmetric_difference([{1, 2}, {2, 3}, {3, 4}]) == {1, 4}


# 7. Set Cardinality and Power Set
def test_calculate_power_set():
    assert calculate_power_set({1, 2}) == {(), (1,), (2,), (1, 2)}


# 8. Set Combination Sum
def test_find_combinations():
    assert find_combinations({2, 3, 5}, 5) == [[2, 3], [5]]


# 9. Venn Diagram
# Note: This test not valid, since each one prints the venn diagram differently.
# Please refer for the solution file.
# This test is a bit challenging to implement directly without seeing the implementation.
# But here's a basic test just to make sure the function runs:
def test_print_venn_diagram():
    pass


# 10. Prime Factorization using Unique Prime Sets
def test_prime_factorization_sets():
    assert are_arrays_equal(prime_factorization_sets(12), [2, 3, 2])
    assert are_arrays_equal(prime_factorization_sets(6), [2, 3])


# helper function
def are_arrays_equal(arr1, arr2):
    return sorted(arr1) == sorted(arr2)


def run_all_tests():
    # test_calculate_factorial()
    # print("Passed test_calculate_factorial")

    # test_increment_counter()
    # print("Passed test_increment_counter")

    # test_check_palindrome()
    # print("Passed test_check_palindrome")

    # test_calculate_sum()
    # print("Passed test_calculate_sum")

    # test_calculate_circle_area()
    # print("Passed test_calculate_circle_area")

    # test_find_symmetric_difference()
    # print("Passed test_find_symmetric_difference")

    # test_calculate_power_set()
    # print("Passed test_calculate_power_set")

    # test_find_combinations()
    # print("Passed test_find_combbinations")

    # test_print_venn_diagram()
    # print("Passed test_print_venn_diagram")

    # test_prime_factorization_sets()
    # print("Passed test_prime_factorization_sets")

    # print("Passed all tests!!!")


run_all_tests()
