class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            left = 0
            count = 0
            res = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    count += 1
                while count > k:
                    if nums[left] % 2 == 1:
                        count -= 1
                    left += 1
                res += right - left + 1
            return res
        
        return atMostK(nums, k) - atMostK(nums, k - 1)
        