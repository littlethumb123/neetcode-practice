# Strategy:
# Create a hash 
# hash[1] = False
# hash[19] = False
# hash[3] = True
# hash[9] = False
# hash[2] = True
# hash[4] = False
# [2,20,4,10,3,4,5]
# set([1,19,3,9,2,4])s

# [0,3,2,5,4,6,1,1]
# [-1,2,1,4,5,0,0]
# sa
# [1,3,2,5,6,7,10,12,14]
# [0,2,1,4,5,6,9,11,13]

# the number of consecutive numbers equals to number of non-duplicated elements exist in the original array plus 1 

# hash[0] = s
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        numset = set(nums)
        max_len = 0
        for i in numset: 
            if i - 1 not in numset: 
                strip = 1
                while i + strip in numset:
                    strip += 1
                max_len = max(max_len, strip)
        return max_len

        