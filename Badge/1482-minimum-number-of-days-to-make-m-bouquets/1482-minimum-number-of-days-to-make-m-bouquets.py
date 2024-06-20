class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)< m*k:
            return -1
        l=min(bloomDay)
        r = max(bloomDay)   
        while l<=r:
            mid=(l+r)//2

            if self.isPossible(bloomDay,mid,m,k) == True:
                r= mid -1
            else:
                l = mid +1

        return l             



    def isPossible(self,bloomDay,day,m,k) -> bool:
        count = 0
        bouquets= 0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=day:
                count+=1
            else:
                bouquets += (count//k) 
                count = 0

        bouquets += (count//k)
        return bouquets >= m           

