class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                diff = prices[r] - prices[l]
                maxdiff = max(diff, maxdiff)
            else:
                l = r
            r += 1
        return maxdiff





        