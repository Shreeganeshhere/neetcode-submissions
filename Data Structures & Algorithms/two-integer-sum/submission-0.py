class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            reqd = target - nums[i]

            if reqd in hash_map:
                return [hash_map[reqd], i]
                
            hash_map[nums[i]] = i
        
        