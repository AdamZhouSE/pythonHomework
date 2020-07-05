class Solution(object):
    def combinationSum3(self, k, n):
        if not k or not n:
            return []
        res = []
        
        def dfs(k, n, tmp, start):
            if n == 0 and k == 0:
                res.append(tmp[:])
                return
            if k <= 0 or n <= 0:
                return
            for i in range(start, 10):
                tmp.append(i)
                dfs(k - 1, n - i, tmp, i + 1)
                tmp.pop()
        dfs(k, n, [], 1)
        print(res)


x = input().split(", ")
k = int(x[0])
n = int(x[1])
s = Solution()
s.combinationSum3(k, n)
