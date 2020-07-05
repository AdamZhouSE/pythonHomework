K=int(input())
N=int(input())
dp=[[0 for i in range(N+1)] for j in range(K+1)]
m=0
while dp[K][m]<N:
    m+=1
    for k in range(K+1):
        dp[k][m]=dp[k][m-1]+dp[k-1][m-1]+1
print(m)