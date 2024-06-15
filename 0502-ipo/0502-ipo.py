class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = list(zip(capital, profits))
        # Sort projects based on the capital required
        projects.sort()

        max_profit_heap = []
        current_index = 0

        for _ in range(k):
        # Push all projects that can be started with the current capital into the max-heap
            while current_index < len(projects) and projects[current_index][0] <= w:
               heapq.heappush(max_profit_heap, -projects[current_index][1])
               current_index += 1

        # If the heap is empty, no further project can be started
            if not max_profit_heap:
               break

        # Pop the project with the maximum profit
            w += -heapq.heappop(max_profit_heap)

        return w
