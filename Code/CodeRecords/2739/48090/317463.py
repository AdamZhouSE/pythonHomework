x=eval(input())
a=x[0]
b=x[1]

class Solution(object):
    def combinationSum3(self, k, n):

        def dfs(i, n, path):
            if n == 0 and len(path) == k: ans.append(path)
            if n <= 0: return

            for j in range(i + 1, 10):
                dfs(j, n - j, path + [j])

        ans = []
        dfs(0, n, [])
        return ans

c=Solution()
print(c.combinationSum3(a,b))