from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True

        return False
