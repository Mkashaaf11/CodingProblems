class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project = []
        for c,p in zip(capital,profits):
            project.append((c,p))

        project.sort()
        heap = []
        i=0

        while k>0:
            while i < len(project) and project[i][0]<=w:
                heapq.heappush(heap,-project[i][1]) 
                i+=1
                
            w+= -heapq.heappop(heap)
            k-=1
                   

        return w
