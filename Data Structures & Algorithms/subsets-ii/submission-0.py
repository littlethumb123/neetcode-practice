# [1,1,2]

class Solution:
    def __init__(self):
        self.res = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtracking(cnt, start, used, path):
            if cnt <= len(nums):
                self.res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1] and used[i] == False: continue
                path.append(nums[i])
                used[i] = True
                backtracking(cnt + 1, i+1, used, path)
                used[i] = False
                path.pop()

        backtracking(0, 0, [False]*len(nums), [])
        return self.res
        