class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        list1 = []
        list2 = []
        result = []
        n = len(nums)
        for i in range(n):
            if nums[i]>0:
                list1.append(nums[i])
            else:
                list2.append(nums[i])


        for i in range(n//2):
            result.append(list1[i])
            result.append(list2[i])

        return result
        