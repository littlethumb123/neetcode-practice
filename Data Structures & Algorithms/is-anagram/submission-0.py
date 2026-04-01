class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        res_cnt = len(t)
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
    
        for i in t:
            if i not in s_dict: return False
            s_dict[i] -= 1
            if s_dict[i] < 0: return False

        return all([i == 0 for i in s_dict.values()])
        