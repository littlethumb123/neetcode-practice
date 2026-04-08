# For each element, find the next element that is greater than it. 
# 3, 2, 1, 4, 3, 5
# [3, 2, 1] if 4 comes in and greater than the max
# pop the element 
# [4, 3

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        que = deque([(0, temperatures[0])])
        max_val = temperatures[0]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while que and que[-1][1] < temperatures[i]:
                pos, val = que.pop()
                res[pos] = i - pos
            que.append((i, temperatures[i]))
        return res

        