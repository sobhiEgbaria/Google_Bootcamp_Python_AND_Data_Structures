from Assignment2_solution import *

COUNT_FAILS = 0
GRADE = 110
TESTS_RESULT_FILE_NAME = "test_result.txt"


def assert_equal(actual, expected, msg, deduction=0.0):
    global COUNT_FAILS
    global GRADE
    if expected != actual:
        COUNT_FAILS += 1
        GRADE += deduction
        msg = f"{COUNT_FAILS}) {msg}, Expected: {expected}, but got: {actual}. ({deduction})"
        print(msg)
        with open(TESTS_RESULT_FILE_NAME, "a") as test_result_file:
            test_result_file.write(f"{msg}\n")


def test_flatten_list():
    assert_equal(flatten_list([]), [], "flatten_list([])", -2.5)
    assert_equal(flatten_list([1, 2, 3]), [1, 2, 3], "flatten_list([1, 2, 3])", -2.5)
    assert_equal(flatten_list([1, ['2', True, 3], 4]), [1, '2', True, 3, 4], "flatten_list([1, ['2', True, 3], 4])",
                 -2.5)
    assert_equal(flatten_list([[1, 2], [3, [4, 5]], 6]), [1, 2, 3, 4, 5, 6], "flatten_list([[1, 2], [3, [4, 5]], 6])",
                 -2.5)
    assert_equal(flatten_list([[[[1]], 2], 3, 4]), [1, 2, 3, 4], "flatten_list([[[[1]], 2], 3, 4])", -2.5)
    assert_equal(flatten_list([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5], "flatten_list([1, [2, [3, [4, [5]]]]])", -2.5)
    assert_equal(flatten_list([[1, 2], [3, [4, [5]]], 6, [7, [8, [9]]]]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 "flatten_list([[1, 2], [3, [4, [5]]], 6, [7, [8, [9]]]])", -2.5)
    assert_equal(flatten_list([['apple', 'banana'], [[None], ['cherry', [5, 'grape'], {12: 24}]], 'orange']),
                 ['apple', 'banana', None, 'cherry', 5, 'grape', {12: 24}, 'orange'],
                 "flatten_list([['apple', 'banana'], [[None], ['cherry', [5, 'grape'], {12: 24}]], 'orange'])", -2.5)


def test_min_edit_distance():
    word1 = "intention"
    word2 = "execution"
    assert_equal(min_edit_distance(word1, word2), 5, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "kitten"
    word2 = "sitting"
    assert_equal(min_edit_distance(word1, word2), 3, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "horse"
    word2 = "ros"
    assert_equal(min_edit_distance(word1, word2), 3, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "abcdef"
    word2 = "azced"
    assert_equal(min_edit_distance(word1, word2), 3, f"min_edit_distance({word1}, {word2})", -2)

    word1 = ""
    word2 = "abcd"
    assert_equal(min_edit_distance(word1, word2), 4, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "abc"
    word2 = ""
    assert_equal(min_edit_distance(word1, word2), 3, f"min_edit_distance({word1}, {word2})", -2)

    word1 = ""
    word2 = ""
    assert_equal(min_edit_distance(word1, word2), 0, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "abc123"
    word2 = "abc123"
    assert_equal(min_edit_distance(word1, word2), 0, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "abc"
    word2 = "def"
    assert_equal(min_edit_distance(word1, word2), 3, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "abcdff"
    word2 = "cbawdef"
    assert_equal(min_edit_distance(word1, word2), 4, f"min_edit_distance({word1}, {word2})", -2)

    word1 = "banana_and_apple"
    word2 = "banana_apple_and-banana"
    assert_equal(min_edit_distance(word1, word2), 12, f"min_edit_distance({word1}, {word2})", -2)


def test_bank_account():
    account = BankAccount("123456789", 1000.0)
    b = account.get_balance()
    num = account.account_number
    res = f"BankAccount balance: {b}, account number: {num}"
    assert_equal(res, "BankAccount balance: 1000.0, account number: 123456789", "init failed", -2.5)

    account.deposit(500.0)
    assert_equal(account.get_balance(), 1500.0, "BankAccount.deposit(500) and get_balance()", -2.5)

    account.withdraw(200.0)
    assert_equal(account.get_balance(), 1300.0, "BankAccount.withdraw(200) and get_balance()", -2.5)

    account.withdraw(1500.0)
    assert_equal(account.get_balance(), -200.0,
                 "BankAccount.withdraw(1500) and get_balance()", -2.5)


def test_longest_path():
    mat = [[]]
    assert_equal(longest_path(mat), 0, f"longest_path {mat}", -1)

    mat = [[1, 2, 3],
           [6, 5, 4],
           [7, 8, 9]]
    assert_equal(longest_path(mat), 9, f"longest_path {mat}", -1)

    mat = [[1, 2, 3],
           [9, 12, 6],
           [10, 11, 9]]
    assert_equal(longest_path(mat), 4, f"longest_path {mat}", -1)

    mat = [
        [1, 3, 2],
        [6, 4, 7],
        [5, 8, 9]
    ]
    assert_equal(longest_path(mat), 3, f"longest_path {mat}", -1)

    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    assert_equal(longest_path(mat), 3, f"longest_path {mat}", -1)

    mat = [
        [1]
    ]
    assert_equal(longest_path(mat), 1, f"longest_path {mat}", -1)

    mat = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    assert_equal(longest_path(mat), 25, f"longest_path {mat}", -1)

    mat = [
        [1, 2, 3, 4, 5],
        [14, 13, 12, 11, 6],
        [15, 16, 17, 10, 7],
        [8, 9, 18, 19, 8],
        [7, 6, 5, 4, 20]
    ]
    assert_equal(longest_path(mat), 10, f"longest_path {mat}", -1)

    mat = [
        [14, 13, 12, 11, 6],
        [15, 16, 18, 10, 7],
        [8, 9, 18, 19, 8],
        [7, 6, 5, 4, 20]
    ]
    assert_equal(longest_path(mat), 7, f"longest_path {mat}", -1)

    mat = [
        [3, 4, 5],
        [2, 7, 6]
    ]
    assert_equal(longest_path(mat), 6, f"longest_path {mat}", -1)


def create_report_file():
    global TESTS_RESULT_FILE_NAME
    with open("Assignment2_solution.py") as solution_file:
        student_name = solution_file.readline()
        student_name = student_name.replace("#", "")
        student_name = student_name.strip()
        student_name = student_name.replace(" ", "_")
        TESTS_RESULT_FILE_NAME = f"test_result_{student_name}.txt"
    # create and clear the files content
    with open(TESTS_RESULT_FILE_NAME, "w") as file:
        pass


def sum_up_report():
    if COUNT_FAILS == 0:
        print(f"Passed All Tests!\nTests Grade: {GRADE}")
        with open(TESTS_RESULT_FILE_NAME, "a") as test_result_file:
            test_result_file.write(f"Passed All Tests!\nTests Grade: {GRADE}\n")
    else:
        print(f"Failed In {COUNT_FAILS} Tests,\nTests Grade: {GRADE}")
        with open(TESTS_RESULT_FILE_NAME, "a") as test_result_file:
            test_result_file.write(f"Failed In {COUNT_FAILS} Tests\nTests Grade: {GRADE}\n")
        print("test_result.txt file was created with the tests results")

    print("""
**************************************************
GRADES ARE STARTING FROM 110 BECAUSE OF THE BONUS.
FOR THOSE WHO DIDNT DO THE longest_path BONUS
Tests Grade = Tests Grade - 10
**************************************************
    """)


if __name__ == '__main__':
    create_report_file()

    test_flatten_list()
    test_min_edit_distance()
    test_bank_account()
    test_longest_path()

    sum_up_report()
