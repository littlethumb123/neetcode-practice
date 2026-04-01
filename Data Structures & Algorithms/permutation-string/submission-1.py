# create a hash for s1 and record the freq of each element
# use a fixed sliding window
# the sliding window only start at the position where the str2 element shows up in str1
# TC: O(N)
# SC: O(N)
class Solution:
    def is_permute(self, hash, substr):
        hash_c = hash.copy()
        for i in substr:
            if i not in hash_c: return False
            elif hash_c[i] == 0: return False
            else: hash_c[i] -= 1
        return all(i == 0 for i in hash_c.values())

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        hash = {}
        for i in s1:
            hash[i] = hash.get(i, 0) + 1
        l = 0
        while l <= len(s2) - len(s1):
            if s2[l] in hash and self.is_permute(hash, s2[l: l + len(s1)]): 
                    return True
            l += 1
            
        return False
            
            # if l in hash; tehn extract the substr with a lenght of l + 
# Dry run
# s1 = "abc", s2 = "lecabee"
# hash = a = 1, b=1, c = 1
# l = 0, len(s2) = 7, len(s1) = 3
# while l <= 4:
#     # l = 2
#     is_permute(s2[2: 5], hash)

            
        