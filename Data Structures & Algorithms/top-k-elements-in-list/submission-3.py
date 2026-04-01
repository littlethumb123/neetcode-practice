# create frequency N, N
# Counter -> klogk + (n-k)

# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         num_freq = Counter(nums)
#         return [i[0] for i in num_freq.most_common(k)]


# Using heapq heapify entire list
# TC: O(N) + O(NlogN) + O(k)
# Using heapq heapify only k elements
# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         num_freq = defaultdict(int)
#         for i in nums:
#             num_freq[i] += 1
#         num_list = [(freq, num) for num, freq in num_freq.items()]
#         heapq.heapify_max(num_list)
#         return [heapq.heappop_max(num_list)[1] for _ in range(k)]

# TC: O(N) + O(Nlogk)
# TC: O(N) + O(K)
class Solution:
    def topKFrequent(self, nums, k):
        num_freq = defaultdict(int)
        for i in nums:
            num_freq[i] += 1
        k_res = []
        heapq.heapify(k_res)
        cnt = 0
        for val, freq in num_freq.items():
            heapq.heappush(k_res, (freq, val))
            cnt += 1
            if cnt == k + 1:
                heapq.heappop(k_res)
                cnt -= 1
        return [i[1] for i in k_res]




