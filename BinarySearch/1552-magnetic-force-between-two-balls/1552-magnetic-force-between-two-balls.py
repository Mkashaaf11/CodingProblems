class Solution:
    def isPossible(self,force:int, position: List[int], m: int) -> bool:
        prev = position[0]
        ballCount=1
        for i in range(1,len(position)):
            curr = position[i]
            if curr-prev >= force:
                prev = position[i]
                ballCount+=1

            if ballCount == m:
                break
        return ballCount == m            
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = position[len(position)-1] - position[0]
        maxForce = 0

        while low<=high:
            force = low + (high-low)//2
            if self.isPossible(force,position,m):
                maxForce = force
                low = force+1
            else:
                high = force -1    
        return maxForce