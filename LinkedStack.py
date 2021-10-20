class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        # self.first = None

    def add_first(self, data):
        n = Node(data)
        if self.head is None:  # List is empty
            self.head = n
        else:
            nxt = self.head
            self.head = n
            self.head.next = nxt
        self.length += 1

    def delete_first(self):
        curr_node = self.head
        if curr_node is not None:  # if list is not empty
            next_node = curr_node.next
            self.head = next_node
            self.length -= 1


class Stack:
    def __init__(self, size):
        self.maxsize = size
        self.stack = LinkedList()

    def push(self, d):
        if self.stack.length <= self.maxsize:
            self.stack.add_first(d)

    def pop(self):
        if not self.is_empty():
            self.stack.delete_first()

    def peek(self):
        return self.stack.head.data

    def is_empty(self):
        if self.stack.head is None:
            return True
        return False


if __name__ == "__main__":
    my_stack = Stack(10)
    my_stack.push(16)
    my_stack.push(23)
    my_stack.pop()
    print(my_stack.peek())
    print(my_stack.is_empty())


