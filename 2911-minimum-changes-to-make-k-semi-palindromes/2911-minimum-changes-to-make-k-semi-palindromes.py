class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[0] * n for _ in range(n)]

        # Precompute minimum changes for every substring
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        left = start + r
                        right = start + length - d + r

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[start][start + length - 1] = best

        # DP: divide the string into exactly k semi-palindromes
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for groups in range(1, k + 1):
            for end in range(groups * 2, n + 1):
                for start in range((groups - 1) * 2, end - 1):
                    dp[groups][end] = min(
                        dp[groups][end],
                        dp[groups - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]