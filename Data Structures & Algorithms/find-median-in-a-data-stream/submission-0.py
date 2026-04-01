import heapq
class MedianFinder:
    # data structure: 
    # Heap? doubly linked list?
    # insert the element with logn
    # update the mediian with logn
    # two heap; 
    # small and big heap save half of the element
    # if small_cnt == big_cnt: add to big
    # if small_cnt + 1 == big_cnt: add to small
    # if small_cnt == big_cnt: return average
    # else return big heappop
    def __init__(self):
        self.small = []
        self.big = []
        self.small_cnt = 0
        self.big_cnt = 0
        self.median = 0
        heapq.heapify(self.small)
        heapq.heapify(self.big)
        
    def addNum(self, num: int) -> None:
        if num >= self.median:
            heapq.heappush(self.big, num)
            self.big_cnt += 1
            if self.big_cnt - self.small_cnt > 1:
                heapq.heappush(self.small, -heapq.heappop(self.big))
                self.big_cnt -= 1
                self.small_cnt += 1
        else:
            heapq.heappush(self.small, -num)
            self.small_cnt += 1
            if self.small_cnt - self.big_cnt > 0:
                heapq.heappush(self.big, -heapq.heappop(self.small))
                self.big_cnt += 1
                self.small_cnt -= 1

        if (self.small_cnt + self.big_cnt) % 2 == 0:
            self.median = (-self.small[0] + self.big[0]) / 2
        else:
            self.median = self.big[0]
        
    def findMedian(self) -> float:
        return self.median
        
        