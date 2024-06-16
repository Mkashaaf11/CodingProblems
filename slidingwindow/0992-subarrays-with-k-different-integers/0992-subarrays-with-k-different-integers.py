class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindow(nums, k) - self.slidingWindow(nums, k - 1)

    def slidingWindow(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        i = 0
        j = 0
        count = 0
        while j < len(nums):
            hashmap[nums[j]] += 1

            while len(hashmap) > k:
                hashmap[nums[i]] -= 1
                if hashmap[nums[i]] == 0:
                    del hashmap[nums[i]]
                i += 1

            count += (j - i + 1)
            j += 1
        return count
