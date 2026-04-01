1, 1, 2, 8
48, 24, 6, 1

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for i in range(1, len(nums)):
            # last element * most recent prefix value
            # [1, 1, 2, 8]
            # [1, -1, 0, 0, 0]
            prefix[i] = nums[i-1]*prefix[i-1]
        print(prefix)
        for i in range(len(nums)-2, -1, -1):
            # [0, 6, 6, 3, 1]
            suffix[i] = nums[i+1]*suffix[i+1]
        print(suffix)
        return [prefix[i]*suffix[i] for i in range(len(nums))]
        
        