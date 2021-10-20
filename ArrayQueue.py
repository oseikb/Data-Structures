class ArrayQueue:
    def __init__(self, size):
        self.maxsize = size
        self.queue = []

    def enqueue(self, d):
        if not self.is_full():
            self.queue.append(d)

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)

    def display_queue(self):
        for q in self.queue:
            print(q)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def is_full(self):
        if len(self.queue) == self.maxsize:
            return True
        return False

    def peek_front(self):
        return self.queue[0]


if __name__ == "__main__":
    arr_queue = ArrayQueue(5)
    arr_queue.enqueue(5)
    arr_queue.enqueue(15)
    arr_queue.enqueue(25)
    arr_queue.enqueue(35)
    arr_queue.enqueue(45)
    arr_queue.dequeue()
    arr_queue.dequeue()
    arr_queue.enqueue(55)
    arr_queue.display_queue()
    print(arr_queue.peek_front())
    print(arr_queue.is_full())
