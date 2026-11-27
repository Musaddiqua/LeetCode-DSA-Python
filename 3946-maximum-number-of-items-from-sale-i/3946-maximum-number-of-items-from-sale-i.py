from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)

        dp = [0] * (budget + 1)

        for i in range(n):
            factor, price = items[i]

            # Purchased copy + all free copies unlocked
            value = 0

            for j in range(n):
                if items[j][0] % factor == 0:
                    value += 1

            # 0/1 Knapsack: buy this item type at most once
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + value)

        # Spend remaining budget on the cheapest item
        answer = 0

        for b in range(budget + 1):
            extra = (budget - b) // min_price
            answer = max(answer, dp[b] + extra)

        return answer