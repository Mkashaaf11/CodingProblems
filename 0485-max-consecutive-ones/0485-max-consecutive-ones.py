class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        maxcount = 0

        for i in range(n):
            if nums[i]==0:
                maxcount = max(maxcount,count)
                count = 0
            if nums[i] == 1:
                count+=1
        return max(maxcount,count)            

        