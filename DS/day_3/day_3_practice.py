# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

#     def set_data(self, x):
#         self.data = x

#     def set_next(self, next):
#         self.next = next

#     def get_data(self):
#         return self.data

#     def get_next(self):
#         return self.next

#     def __repr__(self):
#         return str(self.data)

# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def insert_first(self, x):
#         self.head = Node(x, self.head)

#     def insert(self, i, x):
#         current = self.head
#         if i == 0:
#             self.insert_first(x)
#         else:
#             current = self.head
#             while i-1 > 0:
#                 current = current.get_next()
#                 i -= 1
#             n = Node(x, current.get_next())
#             current.set_next(n)

#     def remove_first(self):
#         if self.head != None:
#             self.head = self.head.get_next()

#     def remove_at(self,i):
#         if i == 0:
#             self.remove_first()
#         if i > self.__len__():
#             return None
#         current = self.head
#         count = 0
#         while count < i - 1:
#             count += 1
#             current = current.get_next()
#         elem_to_remove = current.get_next()
#         current.set_next(elem_to_remove.get_next())

#         return elem_to_remove.det_data()

#     def __len__(self):
#         current = self.head
#         count = 0
#         while current is not None:
#             count += 1
#             current = current.get_next()

#         return count

# # Recursive len:

# #   def__len__(self):
# #       return recursion_len(self.head)

# # Out of the class:

# # def recursion_len(list_head)
# #     if list_head is None:
# #         return 0
# #     return 1 + recursion_len(list_head.get_next())

#     def find(self, item):
#         index = 0
#         current = self.head
#         while current != None:
#             if current.get_data() == item:
#                 return index
#             index += 1
#             current = current.get_next()

#         return -1

# # Recursive find:

#     #   def find(self, item):
#     #       return find_helper(self.head, item)

# # Out of the class:

# # def find_helper(node, item):
# #     if not node:
# #         return False
# #     if node.get_data() == item:
# #         return True
# #     else:
# #         return find_helper(node.get_next(), item)

#     def remove_last(self):
#         if self.head == None:
#             return None
#         if self.head.get_next() == None:
#             self.head = None
#             return None
#         prev = self.head
#         current = self.head.get_next()
#         while current.get_next() is not None:
#             current = current.get_next()
#         prev.set_next = None
#         return current.get_data()
