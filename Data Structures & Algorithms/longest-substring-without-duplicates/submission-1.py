# Strategy:
# Using a sliding window;
# Always extend the sliding window and only shrink the window when come across repeated element that exist in the window

# TC: O(N)
# SC: O(N) -> keep a set

# z x y z x y z
# lr
# egde condition: only 1 element: return 1

# a b c d e
# z x y z x y z
# a a b b

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1: return len(s)
        left, right = 0, 0
        window = set()
        max_len = 1
        while right < len(s):
            cur_val = s[right]

            while left < right and cur_val in window:
                del_val = s[left]
                window.remove(del_val)
                left += 1
            window.add(cur_val)
            right += 1
            max_len = max(max_len, right - left)
        return max_len
        