class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
            if hashmap[nums[i]]> n//2:
                return nums[i]

        