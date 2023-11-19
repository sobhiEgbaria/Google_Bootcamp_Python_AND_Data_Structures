import sys
import io
from CS_day_2 import *


def test_print_numbers_while():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_numbers_while()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"


def test_print_numbers_for():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_numbers_for()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"


def test_count_vowels():
    assert count_vowels("Hello") == 2
    assert count_vowels("HELLO") == 2
    assert count_vowels("Hll") == 0


def test_sum_numbers_while():
    assert sum_numbers_while() == 5050


def test_print_multiplication_table():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_multiplication_table(3)
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "3\n6\n9\n12\n15\n18\n21\n24\n27\n30\n"


def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30, 40, 50]) == 30


def test_print_reverse_string():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_reverse_string("Hello")
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "olleH\n"


def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(4) == False
    assert is_prime(1) == False


def test_filter_strings():
    assert filter_strings(["Hello", "OpenAI", "AI", "ChatGPT"]) == ["OpenAI", "ChatGPT"]
    assert filter_strings(["a", "ab", "abc", "abcd", "abcde", "abcdef"]) == ["abcdef"]


def test_print_triangle():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_triangle(3)
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "  *\n **\n***\n"


def test_print_opposite_triangle():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_opposite_triangle(3)
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "***\n **\n  *\n"


def test_print_combined_pattern():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_combined_pattern(3)
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "  *\n **\n***\n***\n **\n  *\n"


# if __name__ == "__main__":
#     # test_print_numbers_while()
#     # print("Passed test_print_numbers_while")

#     # test_print_numbers_for()
#     # print("Passed test_print_numbers_for")

#     # test_count_vowels()
#     # print("Passed test_count_vowels")

#     # test_sum_numbers_while()
#     # print("Passed test_sum_numbers_while")

#     # test_print_multiplication_table()
#     # print("Passed test_print_multiplication_table")

#     # test_calculate_average()
#     # print("Passed test_calculate_average")

#     # test_print_reverse_string()
#     # print("Passed print_reverse_string")

#     # test_is_prime()
#     # print("Passed test_is_prime")

#     # test_filter_strings()
#     # print("Passed test_filter_strings")

#     # test_print_triangle()
#     # print("Passed test_print_triangle")

#     # test_print_opposite_triangle()
#     # print("Passed test_print_opposite_triangle")

#     # test_print_combined_pattern()
#     # print("Passed test_print_combined_pattern")

#     # print("Passed all tests!!!")