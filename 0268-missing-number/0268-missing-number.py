class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(0,n-1):
            if nums[i+1]!= nums[i] + 1:
                ans = nums[i] + 1
                return ans

        return n        
        