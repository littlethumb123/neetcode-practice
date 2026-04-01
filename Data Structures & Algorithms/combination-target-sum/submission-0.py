class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def backtracking(self, nums, target, start_index):
        # termination
        if sum(self.path) == target:
            self.result.append(self.path[:])
            return
        if sum(self.path) > target:
            return
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, target, i)
            self.path.pop()
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.backtracking(nums, target, 0)
        return self.result

        