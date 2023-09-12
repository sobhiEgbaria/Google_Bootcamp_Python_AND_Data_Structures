from CS_day_1 import *
from unittest.mock import patch
import sys
import io


def test_first_program():
    # Capture the stdout output
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()

    first_program()

    # Restore stdout
    sys.stdout = old_stdout

    expected_output = (
        "|------------------------------|\n"
        "|                              |\n"
        "| My first Python application! |\n"
        "|                              |\n"
        "|------------------------------|\n"
    )

    assert mystdout.getvalue() == expected_output


def test_variables_separate_lines():
    # Capture the stdout output
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()

    variables_separate_lines()

    # Restore stdout
    sys.stdout = old_stdout

    expected_output = "1\n2\n3.14\nFalse\n"
    assert mystdout.getvalue() == expected_output


def test_variables_single_line():
    # Capture the stdout output
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()

    variables_single_line()

    # Restore stdout
    sys.stdout = old_stdout

    expected_output = "1, 2, 3.14, False\n"
    assert mystdout.getvalue() == expected_output


# No tests for question 3.


def test_print_digits():
    # Mock user input
    user_input = "47"

    # Use 'patch' to replace 'input' with our mock input
    with patch("builtins.input", return_value=user_input):
        # Capture the stdout output
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        print_digits()

        # Restore stdout
        sys.stdout = old_stdout

    expected_output = "Units: 7\nTens: 4\n"
    assert mystdout.getvalue() == expected_output


def test_sum_digits():
    # Mock user input
    user_input = "4581"

    # Use 'patch' to replace 'input' with our mock input
    with patch("builtins.input", return_value=user_input):
        # Capture the stdout output
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        sum_digits()

        # Restore stdout
        sys.stdout = old_stdout

    expected_output = "Sum: 18\n"
    assert mystdout.getvalue() == expected_output


# Q5
def test_average():
    # Mock user inputs
    user_inputs = ["5", "10", "15"]

    # Use 'patch' to replace 'input' with a lambda function that returns our mock inputs
    with patch("builtins.input", side_effect=user_inputs):
        # Capture the stdout output
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        average()

        # Restore stdout
        sys.stdout = old_stdout

    expected_output = "The average of the numbers is 10.0\n"
    assert mystdout.getvalue() == expected_output


def test_sec_to_time():
    # Mock user input
    user_input = "3666"

    # Use 'patch' to replace 'input' with our mock input
    with patch("builtins.input", return_value=user_input):
        # Capture the stdout output
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        sec_to_time()

        # Restore stdout
        sys.stdout = old_stdout

    expected_output = "1 : 1 : 6\n"
    assert mystdout.getvalue() == expected_output


def test_concat_str_and_int():
    # Mock user input
    user_input = "10"

    # Use 'patch' to replace 'input' with our mock input
    with patch("builtins.input", return_value=user_input):
        # Capture the stdout output
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        concat_str_and_int()

        # Restore stdout
        sys.stdout = old_stdout

    expected_output = "The number is 10\n"
    assert mystdout.getvalue() == expected_output


if __name__ == "__main__":
    # Run the test for Q1
    test_first_program()
    print("Passed test_first_program")

    # Run the test for Q2
    test_variables_separate_lines()
    print("Passed test_variables_separate_lines")

    # Run the test for Q2b
    test_variables_single_line()
    print("Passed test_variables_single_line")

    # Run the test for Q4
    test_print_digits()
    print("Passed test_print_digits")

    # Run the test for Q5
    test_average()
    print("Passed test_average")

    # Run the test for Q6
    test_sum_digits()
    print("Passed test_sum_digits")

    # Run the test for Q7
    test_sec_to_time()
    print("Passed test_sec_to_time")

    # Run the test for Q8
    test_concat_str_and_int()
    print("Passed test_concat_str_and_int")

    # All tests passed
    print("All tests passed!")
