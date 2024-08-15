class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numset = set(nums)
        length= 0
        maxlength = 0
        curr_element = 0
        for num in numset:
            if num-1 not in numset:
                length = 1
                curr_element = num+1
            while curr_element in numset:
                length+=1
                curr_element+=1

            maxlength = max(maxlength,length)

        return maxlength            
