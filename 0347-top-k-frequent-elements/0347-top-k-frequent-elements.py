from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        counter = []
        result = []

        for n in nums:
            hash[n] += 1
        
        for num, count in hash.items():
            counter.append([count, num])

        counter = sorted(counter, reverse = True)
        for i in range(k):
            result.append(counter[i][1])

        return result