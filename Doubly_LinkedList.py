class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
        # self.first = None

    def insert_node(self, data):
        n = Node(data)
        if self.head is None:  # List is empty
            self.head = n
        else:  # Insert at the end of List
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = n
            n.previous = curr_node
            self.tail = n
        self.length += 1

    def add_first(self, data):
        n = Node(data)
        if self.head is None:  # List is empty
            self.head = n
        else:
            nxt = self.head
            self.head = n
            self.head.next = nxt
            nxt.previous = self.head
        self.length += 1

    def traverse_left(self):
        cnt = 0
        curr_node = self.tail
        while cnt < self.length:
            print(curr_node.data)
            curr_node = curr_node.previous
            cnt += 1

    def traverse_right(self):
        curr_node = self.head
        cnt = 0
        while cnt < self.length:
            print(curr_node.data)
            curr_node = curr_node.next
            cnt += 1


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_node(10)
    new_list.insert_node(28)
    new_list.insert_node(15)
    new_list.add_first(5)

    print(new_list.length)

    new_list.traverse_right()
    new_list.traverse_left()