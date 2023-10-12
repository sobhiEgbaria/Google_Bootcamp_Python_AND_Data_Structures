class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def empty(self):
        return not bool(self.head)

    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def top(self):
        if self.empty():
            return None
        return self.head.data

    def push(self, e):
        new_node = Node(e)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.empty():
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def empty(self):
        return self.front is None

    def size(self):
        temp = self.front
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def get_front(self):
        if self.empty():
            return None
        return self.front.data


# Exercise 3: This code creates a stack and a queue, inserts elements, and then empties them.
def main():
    elements = [7, 3, 8, 2, 1]
    stack = Stack()
    queue = Queue()
    for element in elements:
        stack.push(element)
        queue.enqueue(element)
    print("Stack: ")
    while not stack.empty():
        print(stack.pop())
    print("Queue: ")
    while not queue.empty():
        print(queue.dequeue())


# Double linked list
class DoubleNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None

    def add_first(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = None


class StackWithTwoQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def empty(self):
        return self.q1.size() == 0

    def push(self, data):
        self.q1.enqueue(data)

    def pop(self):
        if self.empty():
            return None
        while self.q1.size() != 1:
            self.q2.enqueue(self.q1.dequeue())
        popped = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return popped


class QueueWithTwoStacks:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def empty(self):
        return self.s1.size() == 0 and self.s2.size() == 0

    def enqueue(self, data):
        while self.s1.size() != 0:
            self.s2.push(self.s1.pop())
        self.s1.push(data)
        while self.s2.size() != 0:
            self.s1.push(self.s2.pop())

    def dequeue(self):
        if self.empty():
            return None
        return self.s1.pop()


def reverse_queue(q):
    if not q.empty():
        data = q.dequeue()
        reverse_queue(q)
        q.enqueue(data)
    return q


def is_palindrome(dll):
    left = dll.head
    right = dll.tail
    while left != right and right.next != left:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
    return True


def find_middle(dll):
    slow = dll.head
    fast = dll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data
