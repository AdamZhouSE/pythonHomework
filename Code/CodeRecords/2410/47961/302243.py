arr=[int(i) for i in input().split(',')]
difference=int(input())
dp=dict()
for n in arr:
    dp[n]=(dp[n-difference] if n-difference in dp else 0)+1
print(max(dp.values()))