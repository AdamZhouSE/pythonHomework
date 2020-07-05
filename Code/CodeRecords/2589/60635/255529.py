count=int(input())
req=[]
for i in range(count):
    req.append(int(input()))
index=max(req)
dp=[0]*(index+1)
dp[0]=2
dp[1]=1
for i in range(2,index+1):
    dp[i]=dp[i-1]+dp[i-2]
for i in range(count):
    print(dp[req[i]]%1000000007)