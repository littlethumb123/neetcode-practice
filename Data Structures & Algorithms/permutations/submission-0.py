class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtracking(cnt, used):
            if cnt == len(nums):
                self.res.append(self.path[:])
                return
            for i in range(len(nums)):
                if used[i] == True: continue
                used[i] = True
                self.path.append(nums[i])
                backtracking(cnt + 1, used)
                used[i] = False
                self.path.pop()
        backtracking(0, [False]*len(nums))
        return self.res


        