class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        n = len(nums)
        i = 1
        length = 1
        maxLength = 1
        while i<n:
            if nums[i] == nums[i-1]+1:
                length+=1
                maxLength = max(maxLength,length)
            elif nums[i]!=nums[i-1]:
                length=1    


            i+=1
        return maxLength