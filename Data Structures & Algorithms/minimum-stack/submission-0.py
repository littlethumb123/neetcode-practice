# Strategy:
# [(cur_val, min_val)]; 
# cur_val is not the global min but the min by far 
# Push: update min_val and save cur_val
# Pop: pop the top element
# getMin: return the min_val 
# (1, 1), (2, 1), (0, 0), (3, 0)

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            cur_min = self.stack[-1][1]
            self.stack.append((val, min(val, cur_min)))
        else:
            self.stack.append((val, val))
        
    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
