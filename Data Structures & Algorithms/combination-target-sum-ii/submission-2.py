class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtracking(candidates, start, target, used):
            if sum(self.path) > target: return
            if sum(self.path) == target:
                self.res.append(self.path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target: continue
                if i > start and candidates[i] == candidates[i - 1] and used[i-1] == False: continue
                else: 
                    self.path.append(candidates[i])
                    used[i] = True
                    backtracking(candidates, i + 1, target, used)
                    used[i] = False
                    self.path.pop()
        used = [False]*len(candidates)
        backtracking(candidates, 0, target, used)
        return self.res


# Dry run
# start = 0
#     i = 0, continue
#     i = 1, path [2], used[1] = True
# # start = 2
#     i = 2, path [2,2], used[1,2] = True
#     i = 3, path [2,2,4], used[1,2,3] = True, collect
#     jump out of backtracking
#     used[3] = False, path [2,2]
#     i = 4, 

# 