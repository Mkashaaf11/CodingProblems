class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r = max(piles)
        result= r

        while l<=r:
            mid = (l+r)//2
            hour = 0
            for p in piles:
                hour+= math.ceil(p/mid)
            if hour<=h:
                result = min(result,mid)
                r=mid-1    
            else:
                l=mid+1
        return result        