class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums

        def backtracking(start, nums):
            self.res.append(self.path[:])
            for i in range(start, len(nums)):
                self.path.append(nums[i])
                backtracking(i + 1, nums)
                self.path.pop()
        backtracking(0, nums)
        return self.res



# [1], [[1]]
# [1,2], [[1], [1,2]]
# [1,2,3], [[1], [1,2], [1,2,3]]
# [2,3], [[1], [1,2], [1,2,3], [2,3]]



