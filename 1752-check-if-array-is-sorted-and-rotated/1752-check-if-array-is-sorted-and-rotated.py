class Solution:
    def check(self, nums: List[int]) -> bool:
        breakpoint = -1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                breakpoint = i-1
                break
        if breakpoint == -1:
            return True
        for i in range(0,breakpoint):
            if nums[i]>nums[i+1]:
                return False        
        for i in range(breakpoint+1,len(nums)-1):
            if nums[i]>nums[i+1]:
                return False 
        if nums[len(nums)-1]>nums[0]:
            return False

        return True    