# List Node Constructor
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# function print all the linkedLest elements:
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


# add element to the first
def add_to_first(head, value):
    new_node = ListNode(value)
    new_node.next = head
    head = new_node
    return head


# add element to the by index
def add_E_by_index(head, value, index):
    if index == 0:
        return add_to_first(head, value)
    else:
        new_node = ListNode(value)
        cur = head
        counter = 0
        while counter != (index - 1):
            if cur.next is not None:
                cur = cur.next
                counter += 1
            else:
                return add_to_last(head, value)
        new_node.next = cur.next
        cur.next = new_node
    return head


## git element by index:
# def git_E_by_index(head, index):
#     curr = head
#     counter = 0
#     while counter is not index and curr is not None:
#         curr = curr.next
#         counter += 1
#     if curr is not None:
#         print(f"the value in index {index}: {curr.value}")
#     else:
#         print("error")


## git element by value:
# def git_E_by_value(head, value):
#     curr = head
#     index = 0
#     while curr is not None:
#         if curr.value is value:
#             return index
#         curr = curr.next
#         index += 1
#     return -1


## remove any element by value (first med last):
# def remove_any_E_by_value(head, value):
#     prev = None
#     curr = head
#     while curr.value is not value and curr is not None:
#         prev = curr
#         curr = curr.next
#     if curr is None or curr.value is not value:
#         return -1
#     else:
#         if curr is head:
#             head = head.next
#         else:
#             prev.next = curr.next
#     return head


node1 = ListNode(5)
head = node1
tail = head

head = add_E_by_index(head, 1, 0)
head = add_to_last(head, 10)
head = add_to_last(head, 11)
head = add_E_by_index(head, 1111111111111, 4)


print_list(head)

# git_E_by_index(head, 4)

# print(git_E_by_value(head, 3))

# print_list(remove_any_E_by_value(head, 1111111111111)) # bug to fix when e dose not exist


## => => => => => => => => => => => => => => => => => => => => => => => => => => => => => => => => =>

###Doubly Linked Lists


# class D_LinkedListNode:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev


# ## add element to the last:
# def add_to_last(head, value):
#     new_node = D_LinkedListNode(value)
#     if head is None:
#         head = new_node
#     else:
#         curr = head
#         while curr.next is not None:  # while loop => to target the last element
#             curr = curr.next

#         curr.next = new_node  # change the pointer to my new node
#         new_node.prev = curr
#     return head


# # add element to the first
# def add_to_first(head, value):
#     curr = head
#     new_node = D_LinkedListNode(value)
#     new_node.next = curr
#     curr.prev = new_node
#     head = new_node
#     return head


# # add element to the by index
# def insert_by_index(head, value, index):
#     if index == 0:
#         return add_to_first(head, value)
#     else:
#         new_node = D_LinkedListNode(value)
#         cur = head
#         counter = 0
#         while counter != (index - 1) and cur.next is not None:
#             if cur.next is not None:
#                 cur = cur.next
#                 counter += 1
#             else:
#                 return add_to_last(head, value)
#         cur_next = (
#             cur.next
#         )  # the cur is 1 E befor the new_node. the cur_next 1 e after the new_node
#         new_node.next = cur_next
#         cur.next = new_node
#         new_node.prev = cur
#         # cur_next.prev = new_node

#     return head


# D_node2 = D_LinkedListNode(0)
# head = D_node2
# head = add_to_last(head, 10)
# head = add_to_first(head, 1)
# head = insert_by_index(head, 22222222222, 0)
# head = insert_by_index(head, 1111111111111, 4)

# print_list(head)
