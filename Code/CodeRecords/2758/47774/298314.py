n,m=map(int,input().split(' '))
mod = 10007
dp=[0 for i in range(129)]
dpp=[0 for i in range(129)]

dp[0]=1
for i in range(1,n+1):
    dpp[1]=1
    for j in range(1,m+1):
        for k in range(i,-1,-1):
            ans=0
            for l in range(0,k):
                ans+=dp[l]*dpp[k-l]
                ans%=mod
            dpp[k]=ans
    dp[i]=dpp[i]
print(dp[n])