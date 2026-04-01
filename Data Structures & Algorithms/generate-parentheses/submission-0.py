# satisfy the total number of pair of ()
# validity ( must come before ) and the number of ()
# 1, 1, 2, 2, 3
# "(", ")"
# pick 2n times
# pick meet conditions validity of the the string
# valid 
# n = 3
# path = []
# i = 0, e = '(', valid_left = 0 + 1, 
# ((()))
# (()())
# (())()
# ()(())
# ()()()

# (())
# ()()





class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(valid_left, right, n, path):
            if valid_left == n and len(path) == 2*n: 
                res.append(''.join(path[:]))
                return
            for i, e in enumerate(["(", ")"]):
                # condition check
                if valid_left == right and e == ")": break
                if valid_left == n and e == "(": continue
                if e == '(': valid_left += 1 
                if e == ')': right += 1
                path.append(e)
                dfs(valid_left, right, n, path)
                path.pop()
                if e == ')': right -= 1
                if e == '(': valid_left -= 1
        dfs(0, 0, n, [])
        return res
        