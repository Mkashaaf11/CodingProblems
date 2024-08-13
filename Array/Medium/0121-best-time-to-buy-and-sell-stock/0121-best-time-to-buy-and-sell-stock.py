class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr_min = prices[0]
        max_profit = 0
        for i in range(n):
            curr_min = min(curr_min,prices[i])
            max_profit = max(max_profit,prices[i]-curr_min)
        return max_profit    

        