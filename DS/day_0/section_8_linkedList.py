## linkedList


# List Node Constructor
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


## function print all the linkedLest elements:
def print_list(head):
    while head is not None:
        print(head.value)
        head = head.next


## add element to the last:
def add_to_last(head, value):
    new_node = ListNode(value)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:  # while loop => to target the last element
            curr = curr.next
        curr.next = new_node  # change the pointer to my new node
    return head


## git element by index:
def git_E_by_index(head, index):
    curr = head
    counter = 0
    while counter is not index and curr is not None:
        curr = curr.next
        counter += 1
    if curr is not None:
        print(f"the value in index {index}: {curr.value}")
    else:
        print("error")


def git_E_by_value(head, value):  ### NOT WORKING
    curr = head
    index = 0
    while curr is not None:
        if curr.value is value:
            return index
        curr = curr.next
        index += 1
    return -1


def remove_any_E_by_value(head, value):
    prev = None
    curr = head
    while curr.value is not value and curr is not None:
        prev = curr
        curr = curr.next
    if curr is None:
        print("element dose not exist")
    else:
        if curr is head:
            head = head.next
        else:
            prev.next = curr.next
    return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
head = node1

head = add_to_last(head, 50)
# print_list(head)

# git_E_by_index(head, 5)

# print(git_E_by_value(head, 3))

# print_list(remove_any_E_by_value(head, 50))
