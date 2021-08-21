# encoded_number = c1 * new_min + c2 * prev_min = 2 * new_min - prev_min
# c2 = -1, c1 = 2
# decoding => prev_min = 2 * new_min - encoded_number
# PUSH --> Y = 2.X - ME
# POP  --> 2.ME - Y
import math
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.minEle = -math.inf

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            self.s.append(val)
            self.minEle = val
        else:
            if val >= self.minEle:
                self.s.append(val)
            elif val < self.minEle:
                self.s.append((2*val) + ((-1)*self.minEle))
                self.minEle = val
        return

    def pop(self) -> None:
        if len(self.s) == 0:
            return
        else:
            if self.s[-1] >= self.minEle:
                self.s.pop(-1)
            elif self.s[-1] < self.minEle:
                self.minEle = ((2*self.minEle) + ((-1)*self.s[-1]))
                self.s.pop(-1)
        return
    
    def top(self) -> int:
        if len(self.s) == 0:
            return -1
        else:
            if self.s[-1] >= self.minEle:
                return self.s[-1]
            elif self.s[-1] < self.minEle:
                return self.minEle

    def getMin(self) -> int:
        if len(self.s) == 0:
            return -1
        return self.minEle


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
