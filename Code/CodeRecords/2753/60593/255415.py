n=int(input())
flights=eval(input())
src=int(input())
dst=int(input())
K=int(input())
dp=[[100000]*(n+1) for i in range(K+1)]
for k in range(K+1):
    dp[src][k]=0
for flight in flights:
    if(flight[0]==src):
        dp[flight[1]][0]=flight[2]
for k in range(K+1):
    for flight in flights:
        dp[flight[1]][k]=min(dp[flight[1]][k],dp[flight[0]][k-1]+flight[2])
print(-1 if dp[dst][K]==100000 else dp[dst][K])