class Solution:
    # mono stack -> 
    # decreasing from left to right
    # 1, cur = 3 -> pop 1 -> save {1: 3}
    # for the element remaining in the array
    # 4, 2 -> save {4:-1, 2:-1}
    # 4, 3, 2, 5
    # TC: O(N^2)
    # SC: O(N)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = dict()
        mono_stack = []
        for i in nums2:
            while mono_stack and i > mono_stack[-1]:
                temp_val = mono_stack.pop()
                res[temp_val] = i
            mono_stack.append(i)
        return [res.get(i, -1) for i in nums1]

        