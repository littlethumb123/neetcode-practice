class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals
        intervals.sort(key = lambda x: x[0])
        res = []
        low, upper = intervals[0][0], intervals[0][1]
        i = 1
        while i < len(intervals):
            if intervals[i][0] > upper:
                res.append([low, upper])
                low = intervals[i][0]
                upper = intervals[i][1]
            else:
                upper = max(upper, intervals[i][1])
            i += 1
        res.append([low, upper])
        return res        