class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for char in s:
            if char == '(':
                low += 1
                high += 1

            elif char == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # Even the maximum possible '(' count is negative
            if high < 0:
                return False

            # We cannot have fewer than 0 unmatched '('
            low = max(low, 0)

        return low == 0