
dp=dict()
for n in arr:
    dp[n]=(dp[n-difference] if n-difference in dp else 0)+1
return max(dp.values())
