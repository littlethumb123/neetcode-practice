# create a hash for s1 and record the freq of each element
# use a fixed sliding window
# the sliding window only start at the position where the str2 element shows up in str1
# TC: O(N*M)
# SC: O(1): SC for fixed 

# hash1 as the reference to reflect the frequency of s1
# hash2 as the running record of s2 window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        hash1 = [0]*26
        hash2 = [0]*26
        for i in range(len(s1)):
            hash1[ord(s1[i]) - ord('a')] = hash1[ord(s1[i]) - ord('a')] + 1
            hash2[ord(s2[i]) - ord('a')] = hash2[ord(s2[i]) - ord('a')] + 1
        matched = 0
        for i in range(len(hash1)):
            if hash1[i] == hash2[i]: matched += 1

        l = 0
        r = l + len(s1)-1
        #s2[l: r] is the substring with len s1
        #update s2[l] and s2[r] frequency in the hash2
        while r < len(s2)-1:
            if matched == 26: return True     
            # if remove the most left value then equals to the hash1 value then add a match
            left_index = ord(s2[l]) - ord('a')
            if hash2[left_index] - 1 == hash1[left_index]:
                matched += 1
            # if before removing, the numbers are equal; then matched - 1
            elif hash2[left_index] == hash1[left_index]:
                matched -= 1
            hash2[left_index] -= 1
            l +=1
            right_index = ord(s2[r + 1]) - ord('a')
            if hash2[right_index] + 1 == hash1[right_index]:
                matched += 1
            elif hash2[right_index] == hash1[right_index]:
                matched -= 1
            r += 1
            hash2[right_index] += 1
        return matched == 26
            
            


        






            # if l in hash; tehn extract the substr with a lenght of l + 
# Dry run
# s1 = "abc", s2 = "lecabee"
# hash = a = 1, b=1, c = 1
# l = 0, len(s2) = 7, len(s1) = 3
# while l <= 4:
#     # l = 2
#     is_permute(s2[2: 5], hash)

            
        