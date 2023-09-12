""" Python Heap Exercise """

import random
import sys


#########################################
# Question 1 - do not delete this comment
#########################################
class Tank:
    """
    Represents a single tank.
    """

    def __init__(self, serial: str):
        """
        Creates a new tank with a given serial number.
        """
        # TODO: write your code here
        pass

    def serial_number(self) -> int:
        """
        Returns the serial number of the tank.
        """
        # TODO: write your code here
        pass

    def __eq__(self, other: 'Tank') -> bool:
        """
        Checks if self equals another tank.
        This is only true when they have the same serial number
        """
        # TODO: write your code here
        pass

    def __gt__(self, other: 'Tank') -> bool:
        """
        Checks if self is greater than another tank.
        This is only true when self has a larger serial number
        """
        # TODO: write your code here
        pass

    def __lt__(self, other: 'Tank') -> bool:
        """
        Checks if self is less than another tank.
        This is only true when self has a smaller serial number
        """
        # TODO: write your code here
        pass

    def __repr__(self) -> str:
        """
        Returns a string in the following format:
        Tank <serial number>
        where <serial number> should be replaced by the serial number of the tank.

        For example for a tank with serial number "ac" the method should return the string
        "Tank ac"
        """
        # TODO: write your code here
        pass


#########################################
# Question 2 - do not delete this comment
#########################################
class Heap:
    """
    The heap data structure as studied in class.
    Implement it using a list.
    """

    def __init__(self):
        """
        Creates a new empty heap.
        fields are heap, size.
        """
        # TODO: write your code here
        pass

    def __len__(self) -> int:
        """
        Returns the number of tanks in the heap.
        Should operate in O(1).
        """
        # TODO: write your code here
        pass

    def insert(self, t: Tank):
        """
        Inserts a given tank into the heap.
        Should run in time O(log(n)).
        """
        # TODO: write your code here
        pass

    def find_max(self) -> Tank:
        """
        Returns the tank with the highest serial number in the heap.
        Does not change the heap.
        Should run in time O(1).
        """
        # TODO: write your code here
        pass

    def extract_max(self) -> Tank:
        """
        Returns and removes the tank with the highest serial number in the heap.
        Note that this function will change the heap.
        Should run in time O(log(n)).
        """
        # TODO: write your code here
        pass

    def __contains__(self, t: Tank) -> bool:
        """
        Checks if a given tank is a part of the heap.
        """
        # TODO: write your code here
        pass

    def __repr__(self) -> str:
        """
        Returns a string representing all the tanks.
        You may decide for yourselves on the format
        """
        # TODO: write your code here
        pass


#########################################
# Question 3 - do not delete this comment
#########################################
class TankEstimator:
    """
    A class used to estimate the number of produced tanks.
    Keeps all the tanks stored in a heap
    """

    def __init__(self):
        """
        Creates a new estimator with an empty heap.
        """
        # TODO: write your code here
        pass

    def capture_tank(self, t: Tank):
        """
        Adds the data of a new captured tank and puts it in the heap
        """
        # TODO: write your code here
        pass

    def estimate_production(self) -> int:
        """
        Estimates the total number of produced tanks, based on the information of captured tanks.
        Estimation is done according to the formula presented in the assignment's document.
        """
        # TODO: write your code here
        pass


#########################################
# Question 4 - do not delete this comment
#########################################
def simulation(N: int, k: int, T: int) -> int:
    """
    Simulates the production of N tanks.
    Returns the approximation of the number of produced tanks.
    """
    # TODO: write your code here
    # You may use the random module to generate random numbers.
    # Dont change the seed!
    random.seed(42)
    pass


if __name__ == '__main__':
    N, k, T = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    simulation(N, k, T)


#########################################
# Part 2 - do not delete this comment
#########################################

class Node:
    def __init__(self):
        """Initializes a new node."""
        pass


class BinaryHeap:
    def __init__(self):
        """Initializes a new binary heap."""
        pass

    def insert(self, value):
        """
        Inserts a value into the binary heap.

        Parameters:
        - value: The value to be inserted.
        """
        pass

    def percolate_up(self, node):
        """
        Percolates a node up to its proper position in the heap.

        Parameters:
        - node: The node to be percolated up.
        """
        pass

    def max(self):
        """Returns the maximum value in the heap."""
        pass

    def extract_max(self):
        """Removes and returns the maximum value in the heap."""
        pass

    def percolate_down(self, node):
        """
        Percolates a node down to its proper position in the heap.

        Parameters:
        - node: The node to be percolated down.
        """
        pass
