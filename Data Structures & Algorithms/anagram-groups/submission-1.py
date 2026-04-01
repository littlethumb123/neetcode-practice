
# Hashmap
# save independent element combination as key and store the candidates to the values
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        char_dict = defaultdict(list)
        for s in strs:
            char_cnt = [0]*26
            for c in s:
                char_cnt[ord(c) - ord('a')] += 1
            char_dict[tuple(char_cnt)].append(s)
            del char_cnt
        return list(char_dict.values())
