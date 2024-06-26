class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxArea = 0

        while i<j:
            area = min(height[i],height[j]) * (j-i)
            maxArea = max(maxArea,area)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxArea            
        