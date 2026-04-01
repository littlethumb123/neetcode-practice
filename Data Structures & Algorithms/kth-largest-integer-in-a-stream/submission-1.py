import heapq

# Making sure you understand the problem
# add(): when adding the integer val, then returns the kth largest integer (not pop, can be just show)
# Using min heap and save the top k max values
# turn all element to negative and save the first (len+1-k) min values
# at the same we need to store the ones not in the heap
# save a tuple the heap sort by (-ele, ele) -3, -3, -2, -1 the 2nd largest -> the (len+1 - k)th small
# k=3 -> 6 + 1 - 3 = 4 the fourth min value, so store len(nums) + 1 - k to the heap
# 1, 2, 3, 3, 4, 6 -> -1, -2, -3, -3, -4, -6
# 1, 2, 5, 6, 8  k = 2, add 2
# TC O(n*sqrt(k)) + sqrt(k)
# SC O(k)

# Strategy 2:
# Just use heap to store all the negated values and add value and then pops up k when it comes to k; 
# the first k-1 will be added bacm to the heap
# TC O(n*sqrt(n)) + O(ksqrt(k)) ->pop and push back
# I am struggling with where to put the len(nums) - k elements. we still need it
# 1
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heapk = self.heapify_nums(nums)
        

    def heapify_nums(self, nums):
        heap_size = len(nums)
        heapq.heapify(nums)
        while heap_size > self.k:
            heapq.heappop(nums)
            heap_size -= 1
        return nums
            
    def add(self, val):
        # Here should consider the case when the heap is not full
        heapq.heappush(self.heapk, val)
        if len(self.heapk) > self.k:
            heapq.heappop(self.heapk)
        return self.heapk[0]
        
