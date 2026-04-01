# Keep a max heap to store the minimum distance K points
# minimum k distance; 1, 2, 3, 4 -> -1, -2, -3, -4
# TC: O(N) + O(NlogN)
# SC: O(N) + N(k)
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points): return points
        distance = [(self.get_distance(p, (0, 0))*(-1), i) for i, p in enumerate(points)]
        heapq.heapify(distance)
        while len(distance) > k:
            heapq.heappop(distance)
        
        return [points[i] for _, i in distance]

    def get_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        