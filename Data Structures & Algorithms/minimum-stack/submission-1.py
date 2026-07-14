class MinStack:

    def __init__(self):
        self.prefixStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.prefixStack) == 0:
            self.prefixStack.append(val)
        else:
            self.prefixStack.append(min(val, self.prefixStack[-1]))

    def pop(self) -> None:
        self.minStack.pop()
        self.prefixStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.prefixStack[-1]
