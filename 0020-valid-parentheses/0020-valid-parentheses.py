class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs:
                # Closing bracket
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                # Opening bracket
                stack.append(char)

        return len(stack) == 0