# initiate a result list
# 1. insert the element to result to the right position; 
# 2. merge intervals in the result

# TC O(N)
# SC O(N)
# [1, 3, 4, 5], insert 2
# [[1, 3]] new = [2, 4]
# [[1, 3]] new = [3, 4]
# [[1,2],[3,5], ,[7,8], [9,10]], new = [3,9]
# [[1,2],[3,5], ,[7,8], [9,10]], new = [6,10]
# [[1,2],[3,5], ,[7,8], [9,10]], new = [7,10]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        if newInterval[0] > intervals[-1][1]: return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i +=1 
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i +=1
        
        return res

