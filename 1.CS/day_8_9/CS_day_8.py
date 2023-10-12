def subset_sum(arr, sum):
    """
    Given a list of integers 'arr' and an integer 'sum', this method should return a list of all the
    subsets of 'arr' that add up to 'sum'.
    """
    list_length = len(arr)
    index = 0
    current = 0
    sub_set = []
    result = []

    def helper(index, current, sub_set):
        if current == sum:
            result.append(sub_set[:])
            return
        if index >= list_length or current > sum:
            return
        list_index = arr[index]
        sub_set.append(list_index)
        new_index = index + 1
        new_current = current + list_index
        helper(new_index, new_current, sub_set)
        sub_set.pop()

    helper(index, current, sub_set)
    return result


pass


def partition_equal_subset_sum(arr):
    """
    Given a list of integers 'arr', this method should return True if 'arr' can be partitioned into
    two subsets such that the sum of elements in both subsets is equal, otherwise return False.
    """

    pass


def sudoku_solver(board):
    """
    Given a 2D list 'board' representing a Sudoku puzzle, this method should return True if the puzzle
    has a solution, and False otherwise.
    """
    pass


def tug_of_war(arr):
    """
    Given a list of integers 'arr', this method should partition the list into two groups in a way that
    the absolute difference between the sums of the numbers in the groups is minimized. The method should
    return the two groups as two separate lists.
    """
    pass


def coin_change(coins, amount):
    """
    Given a list of integers 'coins' representing coin denominations and an integer 'amount' representing
    a total amount, this method should return the minimum number of coins needed to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    """
    pass
