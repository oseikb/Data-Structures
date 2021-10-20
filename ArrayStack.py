class ArrayStack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = []

    def push(self, d):
        if not self.is_full():
            self.stack.append(d)
            self.top += 1

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            self.top -= 1

    def peek(self):
        return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top == (self.size - 1):
            return True
        return False


if __name__ == "__main__":
    stack = ArrayStack(5)
    stack.push(5)
    stack.push(9)
    stack.push(3)
    stack.push(5)
    stack.push(10)
    stack.push(15)
    #stack.pop()
    print(stack.peek())
    print(stack.is_full())

