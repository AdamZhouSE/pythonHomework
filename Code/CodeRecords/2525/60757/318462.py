start=eval(input())
end=eval(input())
profit=eval(input())
n=len(start)
t=max(end)
dp=[]
for i in range(t+1):
    dp.append(0)
for i in range(1,n+1):
    s=start[i-1]
    e=end[i-1]
    p=profit[i-1]
    for j in range(s+1,e):
        dp[j]=max(dp[j-1],dp[j])
    dp[e]=max(dp[s]+p,dp[e])
print(max(dp))
