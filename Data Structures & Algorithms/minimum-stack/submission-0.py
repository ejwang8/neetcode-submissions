class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)
        

    def pop(self) -> None: # always nonempty
        popped = self.stack.pop()
        self.minStack.pop()
        return popped
        

    def top(self) -> int: # always nonempty
        return self.stack[-1]


    def getMin(self) -> int: # always nonempty
        return self.minStack[-1]
        
