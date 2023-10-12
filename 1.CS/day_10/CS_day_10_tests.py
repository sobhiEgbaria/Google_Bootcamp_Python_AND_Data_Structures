# Assuming the code is in a module called my_module.py
import math
from day_10.CS_day_10_solutions import *
from math import pi
from file_operations import *
from custom_calculator import *
from string_operations import *


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False


def test_add():
    assert add([1, 2, 3]) == 6


def test_multiply():
    assert multiply([2, 3, 4]) == 24


def test_circle():
    c = Circle(5)
    assert math.isclose(c.area(), pi * 5**2)
    assert math.isclose(c.circumference(), 2 * pi * 5)


def test_rectangle():
    r = Rectangle(2, 3)
    assert r.area() == 6
    assert r.perimeter() == 10


def test_employee():
    e = Employee("Alice", 5000)
    assert e.annual_salary() == 60000
    e.raise_salary(10)
    assert e.salary == 5500


def test_student():
    s = Student("Alice", 1)
    s.add_mark("Math", 90)
    s.add_mark("English", 80)
    assert s.get_total_marks() == 170


def run_all_tests():
    test_reverse_string()
    print("Passed test_reverse_string")

    test_is_palindrome()
    print("Passed test_is_palindrome")

    test_add()
    print("Passed test_add")

    test_multiply()
    print("Passed test_multiply")

    test_circle()
    print("Passed test_circle")

    test_rectangle()
    print("Passed test_rectangle")

    test_employee()
    print("Passed test_employee")

    test_student()
    print("Passed test_student")

    print("Passed all tests!!!")


run_all_tests()
