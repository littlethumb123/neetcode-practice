# create frequency N, N
# Counter -> klogk + (n-k)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        return [i[0] for i in num_freq.most_common(k)]
        