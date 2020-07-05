class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        dp = [float('inf') for _ in range(n)]
        dp[src] = 0
        for i in range(K+1):
            tmp = dp[:]
            for u, v, w in flights:
                dp[v] = min(dp[v],tmp[u]+w)
        return dp[dst] if dp[dst] != float('inf') else -1


n = eval(input())
edges = eval(input())
src = eval(input())
dst = eval(input())
k = eval(input())
s = Solution()
print(s.findCheapestPrice(n, edges, src, dst, k))