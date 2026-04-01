# sliding window + hash
# always extend window and shrink window ONLY the window inlucdes all t elements
# TC: O(N) N is the len(s)
# SC: O(M) M is the len(t)




class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        t_hash = {}
        w_hash = {}
        for i in t:
            t_hash[i] = t_hash.get(i, 0) + 1
        met = 0 # indicate how many elements have been met
        l, r = 0, 0
        min_len = len(s) + 1
        res = ""
        while r < len(s):
            add_ele = s[r]
            # if the current added ele in w_hash; then update the window frequency
            if add_ele in t_hash:
                w_hash[add_ele] = w_hash.get(add_ele, 0) + 1
                if w_hash[add_ele] == t_hash[add_ele]: 
                    met += 1
            
            # now starting to shrink the window
            while met == len(t_hash):
                # here record the min_length of the substring
                if r - l + 1 < min_len:
                    res = s[l: r+1]
                    min_len = r + 1 -l 
                del_ele = s[l]
                l += 1
                if del_ele in t_hash:
                    if w_hash[del_ele] == t_hash[del_ele]: met -= 1
                    w_hash[del_ele] -= 1
            r += 1
        return res
        