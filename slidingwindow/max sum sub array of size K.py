class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        sum=0
        mx = float('-inf')
        while j<n:
            sum= sum+nums[j]
            if j-i+1<k:
                j+=1
            else:
                mx = max(mx,sum)
                sum = sum - nums[i]
                i+=1
                j+=1
        return mx

        