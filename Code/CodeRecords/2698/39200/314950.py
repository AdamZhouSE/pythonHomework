n,d=map(int,input().split())
dp=[1]
for i in range(1,d+1):
    dp.append(dp[i-1]**n+1)
if(d==0):
    print(1, end='')
else:
    print(dp[d]-dp[d-1], end='')
