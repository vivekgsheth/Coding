class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.ss = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.ss) == 0 or self.ss[-1] >= val:
            self.ss.append(val)
        return

    def pop(self) -> None:
        if len(self.s) == 0:
            return -1
        ans = self.s[-1]
        self.s.pop(-1)
        if ans == self.ss[-1]:
            self.ss.pop(-1)
        return

    def top(self) -> int:
        if len(self.s) == 0:
            return -1
        return self.s[-1]

    def getMin(self) -> int:
        if len(self.ss) == 0:
            return -1
        return self.ss[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
