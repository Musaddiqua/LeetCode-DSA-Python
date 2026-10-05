class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                value = stack.pop()

                if value == 0:
                    value = 1
                else:
                    value = 2 * value

                stack[-1] += value

        return stack[0]