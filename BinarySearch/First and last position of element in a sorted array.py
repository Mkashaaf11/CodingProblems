class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]


    def binarySearch(self,nums,target,leftbias):
        left = 0
        right = len(nums)-1
        i = -1
        while left<=right:
            middle = (left+right) // 2
            if nums[middle]>target:
                right = middle - 1
            elif nums[middle]<target:
                left = middle + 1
            else:
                i = middle
                if leftbias:
                    right = middle - 1
                else:
                    left = middle + 1
        return i
        