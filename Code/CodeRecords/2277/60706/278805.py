K=int(input())
N=int(input())
dp = range(N+1)
for k in range(2, K+1):
    dp2 = [0]
    x = 1
    for n in range(1, N+1):
        while x < n and max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1]):
            x += 1
        dp2.append(1 + max(dp[x-1], dp2[n-x]))

    dp = dp2
ans=dp[-1]
print(ans)