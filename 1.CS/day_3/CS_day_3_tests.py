import sys
import io
from CS_day_3 import *


def test_print_second_element_tuple():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_second_element_tuple()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "banana\n"


def test_modify_tuple_copy():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    modify_tuple_copy()
    sys.stdout = sys.__stdout__
    assert (
        capturedOutput.getvalue()
        == "('apple', 'banana', 'cherry')\n('apple', 'banana', 'cherry', 'orange')\n"
    )


def test_print_names_with_index():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_names_with_index(["Alice", "Bob", "Charlie"])
    sys.stdout = sys.__stdout__
    assert (
        capturedOutput.getvalue()
        == "Index: 0, Name: Alice\nIndex: 1, Name: Bob\nIndex: 2, Name: Charlie\n"
    )


def test_mutable_immutable_demo():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    mutable_immutable_demo()
    sys.stdout = sys.__stdout__
    assert (
        capturedOutput.getvalue()
        == "(1, 2, 3)\nCannot modify a tuple\n[1, 2, 3]\n[5, 2, 3]\n"
    )


def test_demonstrate_aliasing():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    demonstrate_aliasing()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "[5, 2, 3]\n[5, 2, 3]\n"


def test_print_string_slicing():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_string_slicing("HelloWorld")
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "Hel\nrld\n"


def test_sum_and_product_slicing():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sum_and_product_slicing([1, 2, 3, 4, 5])
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "9\n8\n"


def test_deep_copy_modify_nested_list():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    deep_copy_modify_nested_list()
    sys.stdout = sys.__stdout__
    assert (
        capturedOutput.getvalue()
        == "[[1, 2, 3], [4, 5, 6]]\n[[100, 2, 3], [4, 5, 6]]\n"
    )


def test_month_slicing():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    month_slicing()
    sys.stdout = sys.__stdout__
    assert (
        capturedOutput.getvalue()
        == "('January', 'February', 'March', 'April')\n('May', 'June', 'July', 'August')\n('September', 'October', 'November', 'December')\n"
    )


def test_print_every_second_reverse():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_every_second_reverse([1, 2, 3, 4, 5, 6, 7])
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "[7, 5, 3, 1]\n"


def run_all_tests():
    # test_print_second_element_tuple()
    # print("Passed test_print_second_element_tuple")

    # test_modify_tuple_copy()
    # print("Passed test_modify_tuple_copy")

    # test_print_names_with_index()
    # print("Passed test_print_names_with_index")

    # test_mutable_immutable_demo()
    # print("Passed test_mutable_immutable_demo")

    test_demonstrate_aliasing()
    print("Passed test_demonstrate_aliasing")

    # test_print_string_slicing()
    # print("Passed test_print_string_slicing")

    # test_sum_and_product_slicing()
    # print("Passed test_sum_and_product_slicing")

    # test_deep_copy_modify_nested_list()
    # print("Passed test_deep_copy_modify_nested_list")

    # test_month_slicing()
    # print("Passed test_month_slicing")

    # test_print_every_second_reverse()
    # print("Passed test_print_every_second_reverse")

    # print("Passed all tests!!!")


run_all_tests()
