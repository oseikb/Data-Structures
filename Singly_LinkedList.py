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
            last_node = self.return_last_node()
            last_node.next = n
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

    def return_last_node(self):
        curr_node = self.head
        cnt = 1
        while cnt < self.length:
            curr_node = curr_node.next
            cnt += 1
        return curr_node

    def find_node(self, d):
        curr_node = self.head
        cnt = 0
        while cnt < self.length:
            if curr_node.data == d:
                return curr_node
            curr_node = curr_node.next
            cnt += 1

    def delete_node(self, d):
        curr_node = self.head
        if curr_node is not None:  # if list is not empty
            next_node = curr_node.next
            if curr_node.data == d:  # first node or only node
                self.head = next_node
                self.length -= 1
            else:  # retrieve curr node and next node
                cnt = 1
                while cnt < self.length:
                    if next_node.data == d:
                        self.length -= 1
                        if next_node.next is None:  # last node
                            curr_node.next = None
                        else:
                            curr_node.next = next_node.next
                    next_node = next_node.next
                    curr_node = curr_node.next
                    cnt += 1


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_node(10)
    new_list.insert_node(28)
    new_list.insert_node(15)
    new_list.add_first(5)

    print(new_list.length)
    print(new_list.find_node(11))
    print(new_list.delete_node(10))
    print(new_list.length)
    print(new_list.find_node(15))