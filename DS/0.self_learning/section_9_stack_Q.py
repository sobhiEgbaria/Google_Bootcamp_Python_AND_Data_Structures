"""
stack and queues

stack: ערימה
last in first out(lifo) : 1push 2popo 3isEmpty 4top
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_Empty(self):
        return len(self.stack) == 0  # shortcut to if true and else false

    def get_top(self):
        if self.is_Empty():
            print("the stack is empty")
            return None
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)
        return f"append is done"

    def pop(self):
        if self.is_Empty():
            return f"the stack is empty"

        else:
            self.stack.pop()
            return f"remove is done"


new_stack = Stack()
print(new_stack.push(13))
print(new_stack.push(14))
print(new_stack.push(15))
print(new_stack.get_top())
print(new_stack.pop())
print(new_stack.get_top())
print(new_stack.is_Empty())
