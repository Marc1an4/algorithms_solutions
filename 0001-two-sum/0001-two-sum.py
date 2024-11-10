class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i

        for j in range(len(nums)): 
            current = target - nums[j]
            if current in hash and hash[current] != j:
                return [j, hash[current]]