# sort the nums
# l and r
# if the array has -(nums[l] + nums[r])
# deduplicate
# if 

# -4, -1, -1, 0, 1, 2
# 4: -4, 1: -1, 0: 0, -1: 1, -2: 2

# -5, -5, -1, 0, 5, 6, 6




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0: return []
        res = []
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l-1]: 
                    l +=1
                    continue
                if r < len(nums) - 1 and nums[r] == nums[r + 1]: 
                    r -=1
                    continue
                if nums[l] + nums[r] == - nums[i]: 
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < - nums[i]:
                    l += 1
                elif nums[l] + nums[r] > - nums[i]:
                    r -= 1

        return res