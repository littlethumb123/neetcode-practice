"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# This translate to problem: max number of overlapse
# [(0, 10), (5, 20), (10, 20), (10, 15) (15, 30)]
# No overlap -> 1 room
# max two overlaps -> 2 rooms
# use a dictionary where key is the room key and value is the time frame that can fit that room
# {0: [(0, 20)], 1:[5, 20], 2: }
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals first
        # create list, each element save a (min, max) interval; for each elment in the intervals, add it to the interavl that has no overlap with it. 
        # return the number of element in the list
        if len(intervals) <= 1: return len(intervals)
        intervals.sort(key = lambda i: i.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            use_existing = False
            for j in range(len(res)):
                if intervals[i].start >= res[j].end:
                    res[j].end = intervals[i].end
                    use_existing = True
                    break
            # if they are all overlapped
            # have to add another room
            if not use_existing:
                res.append(intervals[i])
            
        return len(res)





        