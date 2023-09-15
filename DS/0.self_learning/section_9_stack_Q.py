# """
# stack and queues

# stack: ערימה
# last in first out(lifo) : 1push 2popo 3isEmpty 4top
# """


# class Stack:
#     def __init__(self):
#         self.stack = []
#         # self.top = -1

#     def push(self, value):
#         # self.top += 1
#         self.stack.append(value)
#         return f"append is done"

#     def is_Empty(self):
#         return len(self.stack) == 0  # shortcut to if true and else false

#     def get_top(self):
#         if self.is_Empty():
#             print("the stack is empty")
#             return None
#         return self.stack[-1]

#     def pop(self):
#         if self.is_Empty():
#             return f"the stack is empty"

#         else:
#             self.stack.pop()
#             return f"remove is done"


# new_stack = Stack()
# print(new_stack.push(13))
# print(new_stack.push(14))
# print(new_stack.push(15))
# print(new_stack.get_top())
# print(new_stack.pop())
# print(new_stack.get_top())
# print(new_stack.is_Empty())

# implementation stack with linked list ((linked stack))


# class Stack:
#     def __init__(self, value, next=None) -> None:
#         self.value = value
#         self.next = next
#         self.top = None

#     def is_Empty(self):
#         return self.top == 0

#     def push(self, value):
#         new_node = Stack(value)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if self.is_Empty():
#             print("the stack is empty")
#             return None
#         else:
#             self.top = self.top.next

#     def pop_with_save_value(self):
#         if self.is_Empty():
#             print("the stack is empty")
#             return None
#         else:
#             top_value = self.top.value
#             self.top = self.top.next
#         return top_value

#     def get_top(self):
#         if self.is_Empty():
#             print("the stack is empty")
#             return None
#         else:
#             top_value = self.top.value
#         return top_value

#     def display(self):
#         if self.is_Empty():
#             print("the stack is empty")
#             return None
#         else:
#             cur = self.top
#             while cur is not None:
#                 print(cur.value)
#                 cur = cur.next


# new_stack = Stack(10)
# new_stack.push(5)
# new_stack.push(6)
# new_stack.push(7)
# new_stack.pop()
# new_stack.display()
# print(new_stack.get_top())


## => => => => => => => => => => => => => => => => => => => => => => => => => => => => => => => => =>


# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)
#         return f"append is done"

#     def dequeue(self):
#         self.queue.pop(0)
#         return f"remove is done"

#     def first(self):
#         return self.queue[0]


# new_queue = Queue()
# print(new_queue.enqueue(13))
# print(new_queue.enqueue(14))
# print(new_queue.enqueue(15))
# print(new_queue.enqueue(16))
# print(new_queue.enqueue(17))
# print(new_queue.dequeue())
# print(new_queue.first())
