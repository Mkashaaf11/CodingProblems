class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float('-inf')
        n = len(nums)

        for i in range(n):
            
            curr_sum = curr_sum + nums[i]
            if curr_sum < 0:
                curr_sum = 0
            max_sum = max(max_sum,curr_sum)        
        
        return max_sum