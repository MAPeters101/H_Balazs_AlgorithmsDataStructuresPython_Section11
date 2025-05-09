"""
The aim is to design an algorithm that can return the maximum item of a stack
in O(1) running time complexity. We can use O(N) extra memory!

Hint: we can use another stack to track the max item!

Good luck!
"""

class Stack:

    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, data):
        if self.is_empty():
            self.maxStack.append(data)
        elif data > self.maxStack[-1]:
            self.maxStack.append(data)
        else:
            self.maxStack.append(self.maxStack[-1])
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        del self.maxStack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def getMax(self):
        return self.maxStack[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(5)
stack.push(3)
print(stack.getMax())
stack.pop()
print(stack.getMax())
stack.pop()
print(stack.getMax())
stack.pop()
print(stack.getMax())
stack.pop()

