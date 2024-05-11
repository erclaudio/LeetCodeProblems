class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        open_ = '('
        close_ = ')'
        stack = []
        res = []
    
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append(open_)
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(close_)
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0,0)
        return res

            
        