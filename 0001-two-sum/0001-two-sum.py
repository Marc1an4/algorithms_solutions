class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i

        for j in range(len(nums)): 
            current = target - nums[j]
            if nums[hash.get(current, 0)] + nums[j] == target and hash.get(current, 0) != j:
                return [j, hash.get(current)]