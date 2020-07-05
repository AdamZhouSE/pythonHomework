class Solution(object):
    def comb(self, k, n):
        ans = []

        def dfs(k, n, mid, i):
            if n == 0 and k == 0:
                ans.append(mid[:])
                return
            if k <= 0 or n <= 0:
                return
            for i in range(i, 10):
                mid.append(i)
                dfs(k - 1, n - i, mid, i + 1)
                mid.pop()
        dfs(k, n, [], 1)
        return ans


x = input().split(", ")
k = int(x[0])
n = int(x[1])
s = Solution()
print(s.comb(k, n))
