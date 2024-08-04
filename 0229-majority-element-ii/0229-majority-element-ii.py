class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maj1 = None
        maj2 = None
        cnt1 =0
        cnt2=0
        result = []
        for i in range(n):
            if nums[i] == maj1:
                cnt1+=1
            elif nums[i] == maj2:
                cnt2+=1
            elif cnt1==0:
                maj1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0:
                maj2 = nums[i]
                cnt2 = 1
            else:
                cnt1-=1
                cnt2-=1                
        
        freq1 = 0
        freq2 = 0
        for i in range(n):
            if nums[i] == maj1:
                freq1+=1
            if nums[i] == maj2:
                freq2+=1

        if freq1 > n//3:
            result.append(maj1)
        if freq2> n//3:
            result.append(maj2)
        return result                    
