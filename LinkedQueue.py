class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_last(self, data):
        n = Node(data)
        if self.head is None:  # List is empty
            self.head = n
        else:  # Insert at the end of List
            last_node = self.return_last_node()
            last_node.next = n
        self.length += 1

    def delete_first(self):
        curr_node = self.head
        if curr_node is not None:  # if list is not empty
            next_node = curr_node.next
            self.head = next_node
            self.length -= 1

    def return_last_node(self):
        curr_node = self.head
        cnt = 1
        while cnt < self.length:
            curr_node = curr_node.next
            cnt += 1
        return curr_node

    def display_data(self):
        curr_node = self.head
        cnt = 1
        while cnt <= self.length:
            print(curr_node.data)
            curr_node = curr_node.next
            cnt += 1


class Queue:
    def __init__(self, size):
        self.queue = LinkedList()
        self.maxsize = size

    def enqueue(self, d):
        if not self.is_full():
            self.queue.add_last(d)

    def dequeue(self):
        if not self.is_empty():
            self.queue.delete_first()

    def display_queue(self):
        self.queue.display_data()

    def is_empty(self):
        if self.queue.head is None:
            return True
        return False

    def is_full(self):
        if self.queue.length == self.maxsize:
            return True
        return False

    def peek_front(self):
        return self.queue.head.data


if __name__ == "__main__":
    my_queue = Queue(5)
    my_queue.enqueue(5)
    my_queue.enqueue(15)
    my_queue.display_queue()
    print("")
    my_queue.enqueue(25)
    my_queue.enqueue(35)
    my_queue.enqueue(45)
    my_queue.display_queue()
    print("")
    my_queue.dequeue()
    my_queue.dequeue()

    my_queue.enqueue(55)
    my_queue.display_queue()
    print("")
    print(my_queue.peek_front())
    print(my_queue.is_full())