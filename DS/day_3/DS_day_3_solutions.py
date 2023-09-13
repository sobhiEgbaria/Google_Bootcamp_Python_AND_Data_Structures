class PersonNode:
    def __init__(self, name, age, next_node=None):
        self.name = name
        self.age = age
        self.next_node = next_node

    def __repr__(self):
        return f"PersonNode({self.name}, {self.age}, {self.next_node})"


class PersonList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"PersonNode({node.name}, {node.age})")
            node = node.next_node
        nodes.append("None")
        return " -> ".join(nodes)

    def add(self, name, age):
        if not self.head:
            self.head = PersonNode(name, age)
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = PersonNode(name, age)

    def list_length(self):
        def help_length(node: PersonNode):
            if node is None:
                return 0
            return 1 + help_length(node.next_node)

        return help_length(self.head)

    def copy_list(self):
        if self.head is None:
            return None
        copy_list = PersonList()
        node = self.head
        while node:
            copy_list.add(node.name, node.age)
            node = node.next_node
        return copy_list

    def print_line(self):
        print(f"The queue is: {self}")
        print(f"The length of the queue is: {self.list_length()}")

    def is_in_line(self, name):
        node = self.head
        while node is not None:
            if node.name == name:
                return True
            node = node.next_node
        return False

    def add_israeli(self, name, age):
        # Check if the queue is empty
        if self.head is None:
            self.head = PersonNode(name, age)
            return

        # Ask for the names of three friends
        friends = [input("Please enter the name of a friend: ") for _ in range(3)]

        # Check if the friends are in the queue
        previous_node = None
        node = self.head
        friend_in_queue = False
        while node is not None:
            previous_node = node
            if node.name in friends:
                friend_in_queue = True
                break
            node = node.next_node

        # Add the new person to the queue
        if friend_in_queue:
            new_person = PersonNode(name, age, previous_node.next_node)
            previous_node.next_node = new_person
        else:
            previous_node.next_node = PersonNode(name, age)

    def remove(self, name):
        if self.head is None:
            print("The queue is empty!")
            return

        if self.head.name == name:
            self.head = self.head.next_node
            print(f"{name} has been removed from the queue.")
            return

        previous_node = self.head
        node = self.head.next_node

        while node is not None:
            if node.name == name:
                previous_node.next_node = node.next_node
                print(f"{name} has been removed from the queue.")
                return
            previous_node = node
            node = node.next_node

        print(f"There is no person with the name {name} in the queue.")

    def add_VIP(self, name, age):
        self.head = PersonNode(name, age, self.head)
        print(f"{name} has been added to the top of the queue.")

    def reverse_list(self):
        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            next_node = curr_node.next_node
            curr_node.next_node = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node
        print("The queue has been reversed.")

    def contains_loop(self):
        """
        We maintain two pointers, slow_ptr and fast_ptr.
        slow_ptr moves one step at a time while fast_ptr moves two steps at a time.
        If there is a loop in the list, fast_ptr will eventually meet slow_ptr.
        If there is no loop, fast_ptr will reach the end of the list.
        """
        if self.head is None:
            return False

        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next_node is not None:
            slow_ptr = slow_ptr.next_node
            fast_ptr = fast_ptr.next_node.next_node

            if slow_ptr == fast_ptr:
                return True

        return False


def main():
    # Initialize the PersonList
    people_list = PersonList()

    # Ask the user for the length of the list
    list_length = int(input("Please enter the length of the list: "))

    # Ask for the names and ages and add them to the list
    for _ in range(list_length):
        name = input("Please enter a name: ")
        age = int(input("Please enter an age: "))
        people_list.add(name, age)

    # Print the list
    print(f"The list is: {people_list}")

    # Print the length of the list
    print(f"The length of the list is: {people_list.list_length()}")

    # Create and print a copy of the list
    copied_list = people_list.copy_list()
    print(f"The copied list is: {copied_list}")


# Q6
def is_tail(head_x, head_y):
    # If head_y is None, it cannot be a tail of head_x
    if head_y is None:
        return False

    # Create two pointers and set them to the heads of the lists
    node_x = head_x
    node_y = head_y

    # Traverse list X to find node_y
    while node_x is not None and node_x != node_y:
        node_x = node_x.next_node

    # If we reached the end of list X without finding node_y, node_y is not a tail of list X
    if node_x is None:
        return False

    # If we found node_y in list X, traverse the rest of list X and list Y in parallel
    while node_x is not None and node_y is not None:
        if node_x != node_y:
            return False
        node_x = node_x.next_node
        node_y = node_y.next_node

    # If we reached the end of both lists at the same time, node_y is a tail of list X
    if node_y is None and node_x is None:
        return True

    # If we reached the end of list Y before the end of list X, node_y is not a tail of list X
    return False


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, x):
        if not self.head:
            self.head = Node(x)
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(x)

    def __repr__(self):
        nodes = []
        curr_node = self.head
        while curr_node:
            nodes.append(str(curr_node.data))
            curr_node = curr_node.next
        nodes.append("null")
        return " -> ".join(nodes)

    def insert(self, i, x):
        if i == 0:
            new_node = Node(x)
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            for _ in range(i - 1):
                if curr_node is None:
                    raise IndexError("Index out of range")
                curr_node = curr_node.next
            new_node = Node(x)
            new_node.next = curr_node.next
            curr_node.next = new_node

    def remove(self, i):
        if i == 0:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.data
        else:
            curr_node = self.head
            for _ in range(i - 1):
                if curr_node is None:
                    raise IndexError("Index out of range")
                curr_node = curr_node.next
            removed_node = curr_node.next
            if removed_node is None:
                raise IndexError("Index out of range")
            curr_node.next = removed_node.next
            return removed_node.data

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node


class RecursiveLinkedList:
    def __init__(self):
        self.head = None

    def _insert_last(self, x, node=None):
        if not self.head:
            self.head = Node(x)
            return
        if node is None:
            node = self.head
        if node.next is None:
            node.next = Node(x)
        else:
            self._insert_last(x, node.next)

    def insert_last(self, x):
        self._insert_last(x, self.head)

    def __repr__(self):
        return self._repr(self.head) + "null"

    def _repr(self, node):
        if node is None:
            return ""
        else:
            return str(node.data) + " -> " + self._repr(node.next)

    def _insert(self, i, x, node, prev_node=None):
        if i == 0:
            new_node = Node(x)
            new_node.next = node
            if prev_node is None:  # insert at head
                self.head = new_node
            else:
                prev_node.next = new_node
        elif node is None:
            raise IndexError("Index out of range")
        else:
            self._insert(i - 1, x, node.next, node)

    def insert(self, i, x):
        self._insert(i, x, self.head)

    def _remove(self, i, node, prev_node=None):
        if i == 0:
            if prev_node is None:  # remove head
                self.head = node.next
            else:
                prev_node.next = node.next
            return node.data
        elif node is None:
            raise IndexError("Index out of range")
        else:
            return self._remove(i - 1, node.next, node)

    def remove(self, i):
        return self._remove(i, self.head)

    def reverse(self):
        self._reverse(None, self.head)
        return self.head

    def _reverse(self, prev_node, node):
        if node:
            next_node = node.next
            node.next = prev_node
            self._reverse(node, next_node)
        else:
            self.head = prev_node
