class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int: 
        heap = []
        maxprofit = 0
        for i in range(len(difficulty)):
            heap.append((-profit[i],difficulty[i]))
        
        heapq.heapify(heap)
        worker.sort(reverse=True)

        i=0
        while i <len(worker) and len(heap)>0:
            if worker[i]<heap[0][1]:
                heapq.heappop(heap)
            else:
                maxprofit+= -heap[0][0]
                i+=1
        return maxprofit        