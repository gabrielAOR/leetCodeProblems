class Solution(object):
    def maxProfit(self, prices):
        max = 0
        buy = prices[0]
        for i in range(len(prices)-1):
            if prices[i] < buy:
                buy = prices[i]
            if (prices[i+1] - buy) > max:
                max = prices[i+1] - buy
        
        return max
                