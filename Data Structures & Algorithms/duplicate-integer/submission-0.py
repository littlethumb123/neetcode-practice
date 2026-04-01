class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
            if nums_dict[i] > 1: return True
        return False
        