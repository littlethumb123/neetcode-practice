# Strategy
# Question: how many digits at most can be replaced with a element so that we get longest single identical strings. 
# 1. Collect all distinct elements and count frequency
# 2. for each element, the longest consecutive strings
# 3. Max_len = the longest substring with identical element + k -> Wrong;

# Basic logic is for each element, find out its 

# Is it possible the element of the result is not the element with highest frequency; yes; the frequency of elment does not gaurentee a valid answer
# Other example
# ABCABCCBBBAA, k = 1, B, C; k = 2, B; k = 3, B(7)
# ABCDBABCBD
# AAABCA
# ABCACBA
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Within the window; the most frequent element will be the one that constitute the longest length
        The rest will be the one to be replaced. 
        """
        window = {}
        max_len = 0
        l, r = 0, 0
        most_freq = 0 # the most frequent element count
        while r < len(s):
            cur_val = s[r]
            window[cur_val] = window.get(cur_val, 0) + 1
            most_freq = max(most_freq, window[cur_val])
            while r - l + 1 - most_freq > k:
                window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

                

# Dry run:
# Given example XYYX
# char_cnt = [X, Y], k = 2
# i = X, l, r = 0, 0, i_cnt = 0
# 0 < 4: s[0] == X, then i_cnt = 1; l == r so max_len = max(1, 0-0+1) = 1 -> r = 1
# 1 < 4: s[1] == X, then i_cnt = 2; l < r but 2 - 2 < k=2 then skip and max_len = max(1, 1-0+1) = 2 -> r = 2
# 2 < 4: s[2] != X, skip; l < r but 3 - 2 < k=2 then skip and max_len = max(2, 2-0 + 1) = 3 -> r = 3
# 3 < 4: s[3] != X, skip; l < r but 4 - 2 == k=2 then skip and max_len = max(3, 3-0 + 1) = 3 -> r = 4
# Jump out to Y

# Given example AAABABB
# char_cnt = [A, B], k = 1
# i = X, l, r = 0, 0, i_cnt = 0
# 0 < 7: s[0] == A, then i_cnt = 1; l == r so skip; max_len = max(1, 0 - 0 + 1) = 1 -> r = 1
# 1 < 7: s[1] == A, then i_cnt = 2; l < r but 1-0+1 - 1 == 1, skip; max_len = max(2, 1-0+1) = 2 -> r = 2
# 2 < 7: s[2] == A, then i_cnt = 3; l < r but 2-0+1 - 2 == 1, skip; max_len = max(2, 2-0+1) = 3 -> r = 3
# 3 < 7: s[3] != A, l < r and 3-0+1 - 3 == 1, skip; max_len = max(3, 3-0+1) = 4 > r = 4
# 4 < 7: s[4] != A, l < r and 4-0+1 - 3 == 3, jump in, s[l]==A, then i_cnt = 3-1 = 2, l=1; max_len = max(4, 3-1+1) = 4 > r = 5



        