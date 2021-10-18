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
        elif self.tail is None:  # Only 1 node in the list
            self.tail = n
            self.head.next = n
            self.tail.previous = self.head
        else:
            last_node = self.tail
            last_node.next = n
            self.tail = n
            self.tail.previous = last_node
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

    def find_node(self, d):
        curr_node = self.head
        cnt = 0
        while cnt < self.length:
            if curr_node.data == d:
                return curr_node
            curr_node = curr_node.next
            cnt += 1

    def delete_node(self, d):
        rem_node = self.find_node(d)

        if rem_node is not None:
            next_node = rem_node.next
            prev_node = rem_node.previous
            if next_node is None and prev_node is None:  # 1 node in list
                self.head = None
            elif next_node is None:  # last node in list
                prev_node.next = None
                self.tail = prev_node
            elif prev_node is None:  # first node in list
                next_node.previous = None
                self.head = next_node
            else:
                prev_node.next = next_node
                next_node.previous = prev_node
            self.length -= 1


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_node(10)
    new_list.insert_node(28)
    new_list.insert_node(15)
    new_list.add_first(5)
    print(new_list.length)
    print(new_list.delete_node(15))
    print(new_list.length)

    new_list.traverse_right()
    new_list.traverse_left()
