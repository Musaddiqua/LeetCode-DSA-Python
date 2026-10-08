class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0

        for char in s:
            if char == '(':
                # Add '(' only if it is NOT the outermost one
                if balance > 0:
                    result.append(char)
                balance += 1

            else:
                balance -= 1

                # Add ')' only if it is NOT the outermost one
                if balance > 0:
                    result.append(char)

        return ''.join(result)