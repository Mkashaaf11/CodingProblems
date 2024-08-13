class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index = -1

        # Step 1: Find the pivot (first decreasing element from the right)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index == -1:
            # If no pivot is found, reverse the whole array (last permutation case)
            nums.reverse()
            return
        
        # Step 2: Find the element to swap with the pivot
        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                # Step 3: Swap
                nums[index], nums[i] = nums[i], nums[index]
                break

        # Step 4: Reverse the subarray after the pivot index
        nums[index+1:] = reversed(nums[index+1:])
