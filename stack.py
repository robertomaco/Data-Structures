class Stack:
    def __init__(self):
        self.top = None
        self.arr = []
    
    def push(self, value):
        self.arr.append(value)

    def pop(self):
        self.arr.pop()
    
    def printStack(self):
        print self.arr
