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
            n.next = self.head
        else:  # Insert at the end of List
            curr_node = self.head
            cnt = 1
            while cnt < self.length:
                curr_node = curr_node.next
                cnt += 1
            curr_node.next = n
            n.next = self.head
        self.length += 1

    def add_first(self, data):
        n = Node(data)
        if self.head is None:  # List is empty
            self.head = n
            n.next = self.head
        else:
            nxt = self.head
            self.head = n
            self.head.next = nxt
            self.length += 1
            curr_node = self.head
            cnt = 1
            while cnt < self.length:  # i had to change the last element to point to the new head
                curr_node = curr_node.next
                cnt += 1
            curr_node.next = self.head

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

    for i in range(20):  # range(20)
        print(curr.data)
        curr = curr.next
