class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # A complete valid combination
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still have opening brackets available
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' only if there are unmatched '(' brackets
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result