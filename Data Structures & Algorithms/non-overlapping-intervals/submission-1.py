# Strategy
# sort hte array based on the first value
# [1, 2], [2, 3], [3, 4]
# [1, 3], [2, 3], [3, 4]
# [1, 3], [2, 5], [6, 7], [6, 10]
# [1, 3], [2, 4], [2, 5], [3, 6], [4, 6]
# [1, 10], [2, 3], [3, 4], [4, 5], [10, 14] -> very large coverage, remove the largest
# Sort the tuples by the first value 
# As far as there one overlap, has to remove 1
# any cases that have overlaps at the very beginning but [1, 3], [2, 6], [2, 8]
# how to figure out minimum 

# Strategy
# Find patterns: 
# as far as there is an overlap; have to remove the one with lower upper values; to keep more rooms for future overlappings. 
# For example [1, 3], [2, 4], [4, 7]; have to remove the [2, 4] instead of [1, 3]
# When two intervals overlap, keeping the one with the smaller end time leaves more room for future intervals
# Removing the interval with the larger end is always a worse choice, because it blocks more upcoming intervals
# The number of overlaps is the number of range we need to remove
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1: return 0
        intervals.sort(key = lambda i: i[0])
        res = 0
        pre_end = intervals[0][1]
        i = 1
        while i < len(intervals): 
            if pre_end <= intervals[i][0]: 
                pre_end = intervals[i][1]
            else: # When come across overlapping
                pre_end = min(pre_end, intervals[i][1])
                res += 1
            i +=1
        return res


        