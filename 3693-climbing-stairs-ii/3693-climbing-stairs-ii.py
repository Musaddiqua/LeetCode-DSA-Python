from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0, float('inf'), float('inf'), float('inf')]

        for i in range(1, n + 1):
            dp[i % 4] = costs[i - 1] + min(
                dp[(i - 1) % 4] + 1,
                dp[(i - 2) % 4] + 4,
                dp[(i - 3) % 4] + 9
            )

        return dp[n % 4]