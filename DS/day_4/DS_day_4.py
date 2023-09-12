class Node:
    def __init__(self, data=None):
        """ Initializes Node object """


# Exercise 1
class Stack:
    def __init__(self):
        """ Initializes empty Stack object """

    def empty(self):
        """ Returns whether the stack is empty """

    def size(self):
        """ Returns the size of the stack """

    def top(self):
        """ Returns the topmost element (NOT NODE!) of the stack, without removing it from the stack.
         if not exists return None."""

    def push(self, e):
        """ Inserts element e at the top of the stack """

    def pop(self):
        """ Deletes the topmost element of the stack, and returns it. if not exists return None """


# Exercise 2
class Queue:
    def __init__(self):
        """ Initializes empty Queue object """

    def enqueue(self, data):
        """ Adds an item to the queue """

    def dequeue(self):
        """ Removes an item from the queue.
        The items are popped in the same order in which they are pushed FIFO.
        if not exists return None """

    def front(self):
        """ Get the front item from queue, without removing from the queue """

    def size(self):
        """ Returns the size of the queue """


# Exercise 3
def main():
    """ Create a function main that creates a stack, and a queue,
    and then inserts the following elements into both : [7,3,8,2,1].
    Then empty both the stack and queue by removing all elements and printing the elements you remove.
    print the last element removed from the stack, print the last element removed from the queue.
    """


# Exercise 4
class DoublyNode:
    def __init__(self, data=None):
        """ Initializes DoublyNode object """


class DoublyLinkedList:
    def __init__(self):
        """ Initializes DoublyLinkedList object """

    def add_last(self, data):
        """ Adds a new node with the given data at the end of the DoublyLinkedList """

    def add_first(self, data):
        """ Adds a new node with the give data at the beginning of the DoublyLinkedList """


# Exercise 5
class StackWithTwoQueues:
    def __init__(self):
        """ Initializes StackWithTwoQueues object """

    def empty(self):
        """ Returns whether the stack is empty """

    def push(self, data):
        """ Inserts data at the top of the stack """

    def pop(self):
        """ Deletes the topmost element of the stack """


# Exercise 6
class QueueWithTwoStacks:
    def __init__(self):
        """ Initializes QueueWithTwoStacks object """

    def empty(self):
        """ Returns whether the queue is empty """

    def enqueue(self, data):
        """ Adds an item to the queue """

    def dequeue(self):
        """ Removes an item from the queue.
        The items are popped in the same order in which they are pushed.
        if not exists return None """


# Exercise 7
def reverse_queue(q):
    """ Reverses a queue using recursion and returns it"""


# Exercise 8
def is_palindrome(dll):
    """ Checks if a doubly linked list is a palindrome """


# Exercise 9
def find_middle(dll):
    """ Finds the middle node of a doubly linked list """
