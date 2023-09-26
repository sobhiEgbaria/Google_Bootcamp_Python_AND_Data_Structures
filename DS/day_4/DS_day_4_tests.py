from DS_day_4_solutions import *


def test_stack():
    s = Stack()
    assert s.empty() == True
    assert s.size() == 0
    assert s.top() == None
    assert s.pop() == None
    s.push(1)
    assert s.top() == 1
    assert s.size() == 1
    assert s.pop() == 1
    assert s.size() == 0
    print("Passed test_stack")


def test_queue():
    q = Queue()
    assert q.size() == 0
    assert q.dequeue() == None
    q.enqueue(1)
    assert q.get_front() == 1
    assert q.size() == 1
    assert q.dequeue() == 1
    assert q.size() == 0
    print("Passed test_queue")


def test_doubly_linked_list():
    # Create a DoublyLinkedList
    dllist = DoublyLinkedList()

    # Test adding elements to the end of the list
    dllist.add_last(1)
    dllist.add_last(2)
    dllist.add_last(3)

    # Test adding elements to the beginning of the list
    dllist.add_first(0)
    dllist.add_first(-1)

    # Test the elements of the list forwards
    current = dllist.head
    assert current.data == -1
    current = current.next
    assert current.data == 0
    current = current.next
    assert current.data == 1
    current = current.next
    assert current.data == 2
    current = current.next
    assert current.data == 3
    current = current.next
    assert current is None

    # Test the elements of the list backwards
    current = dllist.tail
    assert current.data == 3
    current = current.prev
    assert current.data == 2
    current = current.prev
    assert current.data == 1
    current = current.prev
    assert current.data == 0
    current = current.prev
    assert current.data == -1
    current = current.prev
    assert current is None


def test_stack_with_two_queues():
    s = StackWithTwoQueues()
    assert s.empty() == True
    s.push(1)
    assert s.pop() == 1
    assert s.empty() == True
    print("Passed test_stack_with_two_queues")


def test_queue_with_two_stacks():
    q = QueueWithTwoStacks()
    assert q.empty() == True
    q.enqueue(1)
    assert q.dequeue() == 1
    assert q.empty() == True
    print("Passed test_queue_with_two_stacks")


def test_reverse_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q = reverse_queue(q)
    assert q.dequeue() == 2
    assert q.dequeue() == 1
    print("Passed test_reverse_queue")


def test_is_palindrome():
    dll = DoublyLinkedList()
    dll.add_last(1)
    dll.add_last(2)
    dll.add_last(1)
    assert is_palindrome(dll) == True
    dll.add_last(3)
    assert is_palindrome(dll) == False
    print("Passed test_is_palindrome")


def test_find_middle():
    dll = DoublyLinkedList()
    dll.add_last(1)
    assert find_middle(dll) == 1
    dll.add_last(2)
    assert find_middle(dll) == 1 or find_middle(dll) == 2
    dll.add_last(3)
    assert find_middle(dll) == 2
    dll.add_last(4)
    dll.add_last(5)
    assert find_middle(dll) == 3
    print("Passed test_find_middle")


def run_all_tests():
    test_stack()
    test_queue()
    test_doubly_linked_list()
    test_stack_with_two_queues()
    test_queue_with_two_stacks()
    test_reverse_queue()
    test_is_palindrome()
    test_find_middle()

    print("Passed all tests!!!")


run_all_tests()
