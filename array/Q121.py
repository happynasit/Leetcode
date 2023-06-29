class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = max(prices)
        min_price = min(prices)

        if index(min_price) < index(max_price):
            return max_price - min_price
