class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans= 0
        for i in range(len(nums)):
            for end in range(i,len(nums)):
                sub_array = nums[i:end+1]
                if sum(sub_array) == goal:
                    ans+=1
        return ans            