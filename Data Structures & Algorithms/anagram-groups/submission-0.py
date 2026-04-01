# detemine two strings are anagrams to each other:
#   use hash to represent frequency of each element, also length of string, 
# for each word, create a hash. and each element indicates frequency of char. and compare element by element
# 
# Brute force comparison O(n^2)
# How to compare pairwise element?

# First loop: create hash
# second use pairwise comparison
# For i in range(len(strs) - 1):
#.   for j in range(1, len(strs)):
#        strs

# create a lengh of 26 and value indicate frequency? 
from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = defaultdict(list)
        # M*N to count frequency
        # N
        for st in strs:
            freq = [0]*26
            for s in st:
                freq[ord(s) - ord('a')] += 1
            hash_dict[tuple(freq)].append(st)
        return list(hash_dict.values())


        