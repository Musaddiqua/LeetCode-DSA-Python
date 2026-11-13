from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Optimization: already non-decreasing
        if all(nums[i] >= nums[i - 1] for i in range(1, n)):
            return n * (n + 1) // 2

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Next greater element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Binary lifting
        LOG = n.bit_length()

        up = [[n] * (n + 1) for _ in range(LOG)]
        sm = [[0] * (n + 1) for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]
            sm[0][i] = nums[i] * (nxt[i] - i)

        for j in range(1, LOG):
            prev_up = up[j - 1]
            prev_sm = sm[j - 1]
            curr_up = up[j]
            curr_sm = sm[j]

            for i in range(n + 1):
                mid = prev_up[i]
                curr_up[i] = prev_up[mid]
                curr_sm[i] = prev_sm[i] + prev_sm[mid]

        # Calculate operations for a subarray
        def get_cost(l, r):
            p = l
            total = 0
            limit = r + 1

            for j in range(LOG - 1, -1, -1):
                q = up[j][p]

                if q <= limit:
                    total += sm[j][p]
                    p = q

            if p <= r:
                total += nums[p] * (r - p + 1)

            return total - (prefix[r + 1] - prefix[l])

        # Sliding window + binary search
        ans = 0
        left = 0

        for right in range(n):
            low = left
            high = right

            while low < high:
                mid = (low + high) // 2

                if get_cost(mid, right) <= k:
                    high = mid
                else:
                    low = mid + 1

            left = low
            ans += right - left + 1

        return ans