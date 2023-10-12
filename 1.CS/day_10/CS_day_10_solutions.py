

# Program to use string_operations module
import string_operations

input_str = "madam"
if string_operations.is_palindrome(input_str):
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not a palindrome")



# Program to use custom_calculator module
import custom_calculator

numbers = [2, 3, 4]
print(f"Sum: {custom_calculator.add(numbers)}")
print(f"Product: {custom_calculator.multiply(numbers)}")

from file_operations import *

filename = input("Enter filename: ")
data = input("Enter data: ")
write_to_file(filename, data)
read_data = read_from_file(filename)
print(f"Data read from file: {read_data}")


from datetime import datetime

def get_formatted_date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
    
formatted_date = get_formatted_date()
print(formatted_date)

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def circumference(self):
        return 2 * pi * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return 12 * self.salary

    def raise_salary(self, percentage):
        self.salary += self.salary * percentage / 100


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def get_total_marks(self):
        return sum(self.marks.values())
