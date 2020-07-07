class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0  for i in range(K+1)]
        m = 0
        while dp[K] < N:
            m += 1
            for i in range(K,0,-1):
                dp[i] += dp[i-1] + 1
        return m
a = int(input())
b = int(input())
s = Solution()
print(s.superEggDrop(a,b))