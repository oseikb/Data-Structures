class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
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
        self.length += 1

    def add_first(self, data):
        n = Node(data)
        if self.head is None:  # List is empty
            self.head = n
        else:
            nxt = self.head
            self.head = n
            self.head.next = nxt
        self.length += 1

    def traverse(self):
        pass


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_node(10)
    new_list.insert_node(28)
    new_list.insert_node(15)
    new_list.add_first(5)

    print(new_list.length)

    curr = new_list.head
    count = 0
    while count < new_list.length:
        print(curr.data)
        curr = curr.next
        count += 1

