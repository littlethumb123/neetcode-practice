class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(cur_sum, start, target, path):
            if cur_sum > target: return
            if cur_sum == target:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > target: continue
                path.append(nums[i])
                backtracking(cur_sum + nums[i], i, target, path)
                path.pop()
        backtracking(0, 0, target, [])
        return res