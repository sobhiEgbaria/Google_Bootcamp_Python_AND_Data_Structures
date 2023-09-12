# Question 1
class PersonNode:
    def __init__(self, name, age, next_node=None):
        self.name = name
        self.age = age
        self.next_node = next_node
        pass

    def __repr__(self):
        res = (self.name, self.age)
        return repr(res)


p1 = PersonNode("sobhi", "18")
print(p1)


# # # Question 2
# class PersonList:
#     def __init__(
#         self,
#         head=None,
#     ):
#         self.head = head
#         self.next = None
#         pass

#     def __repr__(self):
#         res = (self.name, self.age)
#         return repr(res)

#     pass

#     def add(self, name, age):
#         new_person = PersonList(name, age)
#         if self.head is None:
#             self.head = new_person

#         last = self.head
#         while last is not None:
#             last = last.next

#         last.next = new_person

#     pass

#     def list_length(self):
#         current = self.head
#         count = 0
#         while current is not None:
#             count += 1
#             current = current.next
#         return count

#     pass

#     def copy_list(self):
#         """
#         Create and return a deep copy of the list. Do not use the copy module of python.
#         """
#         pass


# p1 = PersonList.add(("gogo"), ("18"))
# print(p1)

# #     # Question 4
# #     def print_line(self):
# #         """
# #         Print the queue and its length.
# #         """
# #         pass

# #     def is_in_line(self, name):
# #         """
# #         Check if a person with the given name is in the queue.
# #         """
# #         pass

# #     def add_israeli(self, name, age):
# #         """
# #         Add a new Israeli person to the queue.
# #         """
# #         pass

# #     def remove(self, name):
# #         """
# #         Remove a person with the given name from the queue.
# #         """
# #         pass

# #     def add_VIP(self, name, age):
# #         """
# #         Add a VIP person to the top of the queue.
# #         """
# #         pass

# #     def reverse_list(self):
# #         """
# #         Reverse the order of the list.
# #         """
# #         pass

# #     # Question 5
# #     def contains_loop(self):
# #         """
# #         Check if the list contains a loop.
# #         """
# #         pass


# # # Question 3
# # def main():
# #     """
# #     Main function to demonstrate the usage of the PersonList class.
# #     """
# #     pass


# # # Question 6
# # def is_tail(head_x, head_y):
# #     """
# #     Check if head_y is a tail of head_x.
# #     """
# #     pass


# # class Node:
# #     def __init__(self, data=None):
# #         """
# #         Initialize a node with data and a reference to the next node.
# #         """
# #         self.data = data
# #         self.next = None


# # # Question 7
# # class LinkedList:
# #     def __init__(self):
# #         """
# #         Initialize an empty linked list.
# #         """
# #         pass

# #     def insert_last(self, x):
# #         """
# #         Insert a node with the given data at the end of the list.
# #         """
# #         pass

# #     def __repr__(self):
# #         """
# #         Return a string representation of the entire list.
# #         """
# #         pass

# #     def insert(self, i, x):
# #         """
# #         Insert a node with the given data at the specified index.
# #         """
# #         pass

# # def remove(self, i):
# #     if self.head == None:
# #         return None
# #     if self.head.get_next() == None:
# #         self.head = None
# #         return None
# #     prev = self.head
# #     current = self.head.get_next()
# #     while current.get_next() is not i:
# #         current = current.get_next()
# #         prev.set_next = None
# #         return current.get_data()
# #         pass

# #     def reverse(self):
# #         """
# #         Reverse the order of the list.
# #         """
# #         pass


# # class RecursiveLinkedList:
# #     def __init__(self):
# #         """
# #         Initialize an empty linked list.
# #         """
# #         pass

# #     def insert_last(self, x):
# #         """
# #         Insert a node with the given data at the end of the list.
# #         """
# #         pass

# #     def __repr__(self):
# #         """
# #         Return a string representation of the entire list.
# #         """
# #         pass

# #     def insert(self, i, x):
# #         """
# #         Insert a node with the given data at the specified index.
# #         """
# #         pass

# #     def remove(self, i):
# #         """
# #         Remove and return the data of the node at the specified index.
# #         """
# #         pass

# #     def reverse(self):
# #         """
# #         Reverse the order of the list.
# #         """
# #         pass
