from CS_day_8_solutions import *


def test_subset_sum():
    assert subset_sum([1, 2, 3, 4, 5], 5) == [[1, 4], [2, 3], [5]]


def test_partition_equal_subset_sum():
    assert partition_equal_subset_sum([1, 5, 11, 5]) == True
    assert partition_equal_subset_sum([1, 3, 3]) == False


def test_sudoku_solver():
    valid_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    assert (
        sudoku_solver(valid_board) == True
    )  # assuming the sudoku board has a valid solution

    invalid_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 8, 9],
    ]
    assert (
        sudoku_solver(invalid_board) == False
    )  # assuming the sudoku board has a valid solution


def test_tug_of_war():
    wanted_diff = abs(sum([3, 4, 1]) - sum([2, 2, 1, 1, 2]))
    first_g, sec_g = tug_of_war([3, 1, 4, 2, 2, 1, 1, 2])
    diff = abs(sum(first_g) - sum(sec_g))
    assert diff == wanted_diff

    wanted_diff = abs(sum([2, 3, 4, 5, 6, 7]) - sum([1, 7, 9, 10]))
    first_g, sec_g = tug_of_war([1, 2, 3, 4, 5, 6, 7, 7, 9, 10])
    diff = abs(sum(first_g) - sum(sec_g))
    assert diff == wanted_diff


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1


def run_all_tests():
    test_subset_sum()
    print("Passed test_subset_sum")

    test_partition_equal_subset_sum()
    print("Passed test_partition_equal_subset_sum")

    test_sudoku_solver()
    print("Passed test_sudoku_solver")

    test_tug_of_war()
    print("Passed test_tug_of_war")

    test_coin_change()
    print("Passed test_coin_change")

    print("Passed all tests!!!")


run_all_tests()
