import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2: return stones[0]
        s = [i*(-1) for i in stones]
        heapq.heapify(s)
        while len(s) > 1:
            a = heapq.heappop(s) * (-1)
            b = heapq.heappop(s) * (-1)
            if a == b: continue
            heapq.heappush(s, (a-b)*(-1))
        if len(s) == 0: return 0
        if len(s) == 1: return s[0] * (-1)
        

        