# Problem 1: Shape, Circle, Rectangle, Square, Triangle
class Shape:
    def __init__(self, name):
        """Initializes a shape with a name."""
        pass

    def area(self):
        """Calculates and returns the area of the shape."""
        pass


class Circle(Shape):
    def __init__(self, name, radius):
        """Initializes a circle with a name and radius."""
        pass

    def area(self):
        """Calculates and returns the area of the circle."""
        pass


class Rectangle(Shape):
    def __init__(self, name, length, width):
        """Initializes a rectangle with a name, length, and width."""
        pass

    def area(self):
        """Calculates and returns the area of the rectangle."""
        pass


class Square(Rectangle):
    def __init__(self, name, side_length):
        """Initializes a square with a name and side length."""
        pass

    def area(self):
        """Calculates and returns the area of the square."""
        pass


class Triangle(Shape):
    def __init__(self, name, base, height):
        """Initializes a triangle with a name, base, and height."""
        pass

    def area(self):
        """Calculates and returns the area of the triangle."""
        pass


# Problem 2: Vehicle, Car, Truck
class Vehicle:
    def __init__(self, make, model, year, weight):
        """Initializes a vehicle with make, model, year, and weight."""
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors):
        """Initializes a car with make, model, year, weight, and number of doors."""
        pass


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, payload_capacity):
        """Initializes a truck with make, model, year, weight, and payload capacity."""
        pass


# Problem 3: BankAccount, SavingsAccount
class BankAccount:
    def __init__(self, account_number, balance):
        """Initializes a bank account with account number and balance."""
        pass

    def deposit(self, amount):
        """Deposits an amount into the account."""
        pass

    def withdraw(self, amount):
        """Withdraws an amount from the account."""
        pass


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        """Initializes a savings account with account number and balance."""
        pass

    def add_interest(self, rate):
        """Adds interest to the account balance based on the given rate."""
        pass


# Problem 4: Employee, Manager
class Employee:
    def __init__(self, name, salary):
        """Initializes an employee with name and salary."""
        pass

    def annual_salary(self):
        """Calculates and returns the annual salary."""
        pass

    def apply_raise(self, percentage):
        """Applies a raise to the salary based on the given percentage."""
        pass


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        """Initializes a manager with name, salary, and bonus."""
        pass

    def apply_raise(self, percentage):
        """Applies a raise to the salary based on the given percentage and adds the bonus."""
        pass


# Problem 5: Linear Search
def linear_search(arr, target):
    """Implements linear search to find the index of the target in the array. Returns -1 if not found."""
    pass


# Problem 6: Binary Search
def binary_search(arr, target):
    """Implements binary search to find the index of the target in the array. Returns -1 if not found."""
    pass


# Problem 7: GraphNode
class GraphNode:
    def __init__(self, value):
        """Initializes a graph node with a value and an empty neighbors list."""
        pass

    def add_neighbor(self, node):
        """Adds a neighboring node."""
        pass

    def print_neighbor(self, node):
        """Prints the values of the neighboring nodes."""
        pass

    def print_graph(self, node):
        """Prints the entire graph, including neighbors and their neighbors."""
        pass
