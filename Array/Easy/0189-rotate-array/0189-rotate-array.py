class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle case where k might be larger than n
        self.reverseHelp(nums,0,n)
        self.reverseHelp(nums,0,k)
        self.reverseHelp(nums,k,n)

    def reverseHelp(self,nums: List[int],start:int,end:int)-> None:
        i = start
        j = end-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    
        