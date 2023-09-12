# Aviel Nisanov

# Q1


def flatten_list(lst):
    # check if the list is None or empty
    if not lst:
        return []
    # split the list into to get the first element
    head, tail = lst[0], lst[1:]
    if isinstance(head, list):
        # recursively flatten the head and concat with flatten the rest of the list
        return flatten_list(head) + (flatten_list(tail))
    else:
        # head is not a list so wrap it in a list and concat with flatten the rest of the list
        return [head] + flatten_list(tail)


def flatten_list_op2(lst):
    flat = []
    for elem in lst:
        if isinstance(elem, list):
            flat.extend(flatten_list_op2(elem))
        else:
            flat.append(elem)
    return flat


# Q2
def min_edit_distance(word1, word2):
    memo = {}
    # call helper function that will receive indexes for word1, word2 and a memo dict
    return edit_distance_recursive_helper(word1, word2, 0, 0, memo)


def edit_distance_recursive_helper(word1, word2, i, j, memo):
    # check if index i and j were calculated
    if (i, j) in memo:
        return memo[(i, j)]

    # if this condition is true, it means we have processed all characters in word1,
    # and the remaining characters in word2 need to be inserted to match word1.
    # So, the edit distance required would be the length of word2 minus the current index j in word2.
    if i == len(word1):
        return len(word2) - j
    # the same explanation as above
    if j == len(word2):
        return len(word1) - i

    # if this condition is true, it means that both letters are equal,
    # and there is no need to add 1 to the edit distance
    if word1[i] == word2[j]:
        memo[(i, j)] = edit_distance_recursive_helper(word1, word2, i + 1, j + 1, memo)
    else:
        # calculate all the operations available
        insert = 1 + edit_distance_recursive_helper(word1, word2, i, j + 1, memo)
        delete = 1 + edit_distance_recursive_helper(word1, word2, i + 1, j, memo)
        replace = 1 + edit_distance_recursive_helper(word1, word2, i + 1, j + 1, memo)
        # store in the memo the min distance of all operations
        memo[(i, j)] = min(insert, delete, replace)

    return memo[(i, j)]


# Q3
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


# Q4
def longest_path(matrix):
    # get the number of rows and cols, **not necessarily square matrix**
    rows, cols = len(matrix), len(matrix[0])
    # initialize a memo matrix in the size if the given matrix with -1 at each cell
    memo_matrix = [[-1] * cols for _ in range(rows)]

    max_path_length = 0
    # run over each cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # run longest_path_dfs from each cell and get the max length and
            max_path_length = max(
                max_path_length, longest_path_dfs(matrix, memo_matrix, i, j)
            )

    return max_path_length


def indexes_are_valid(matrix, i, j):
    # check if the row i and col j indexes are within the matrix
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def longest_path_dfs(matrix, memo, row, col):
    # check if the length from this cell was already calculated
    if memo[row][col] != -1:
        return memo[row][col]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_length = 1

    # run on each direction: down, up, right, left
    for i, j in directions:
        new_row, new_col = row + i, col + j
        # check if the current direction cell value is one greater
        if (
            indexes_are_valid(matrix, new_row, new_col)
            and matrix[new_row][new_col] == matrix[row][col] + 1
        ):
            # run recursively from current direction and increase direction path by one
            max_length = max(
                max_length, 1 + longest_path_dfs(matrix, memo, new_row, new_col)
            )

    # store the calculated cell length in the memo matrix
    memo[row][col] = max_length

    return max_length
