class Stack:
    def __init__(self):
        self.value = []
        self.top = -1

    def push(self, x):
        self.top += 1
        self.value[self.top] = x

    def pop(self):
        if self.isEmpty():
            exit(1)
        top = self.value[self.top]
        self.top -= 1
        return top

    def peek(self):
        if self.isEmpty():
            exit(1)
        return self.value[self.top]

    def isEmpty(self):
        return self.top+1 == 0