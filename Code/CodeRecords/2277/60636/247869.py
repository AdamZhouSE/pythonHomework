def superEggDrop( K, N):
        if N==0 or N==1 or K==1:
            return N
        dp = [[0]*(K+1) for _ in range(N+1)]
        res = N
        for i in range(1,K+1):
            for j in range(1,N+1):
                res = min(res,1+max(dp[i-1][j-1],dp[i][N-j]))
        return res

k=int(input())
n=int(input())
print(superEggDrop(n,k))