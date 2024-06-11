class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        minLength = float('inf')
        summ = 0

        while j < len(nums):
            summ+= nums[j]
            while summ >= target:
                minLength = min(minLength,j-i+1)
                summ -= nums[i]
                i+=1
                

            j+=1
        return 0 if minLength == float('inf') else minLength  


        