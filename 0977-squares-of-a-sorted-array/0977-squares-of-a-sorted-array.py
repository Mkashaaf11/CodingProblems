class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        k = len(nums)-1
        result = [0]*len(nums)

        while k>=0:
            sq1 = nums[i]*nums[i]
            sq2 = nums[j]*nums[j]

            if sq2>sq1:
                result[k]=sq2
                j-=1
            else:
                result[k]=sq1
                i+=1
            k-=1
        return result            