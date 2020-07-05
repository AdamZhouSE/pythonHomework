n=int(input())
seq1=[int(x) for x in input().split()]
seq2=[int(x) for x in input().split()]
seq3=[int(x) for x in input().split()]
a=[seq1,seq2,seq3,seq3]
dp=[[0]*n for x in range(4)]
for x in range(4):
    dp[x][0]=1
ans=-1
for i in range(1,n):
    for j in range(0,i):
        for k in range(0,4):
            if a[0][i]>=a[k][j]:
                dp[0][i]=max(dp[0][i],dp[k][j]+1)
            if a[1][i]<=a[k][j]:
                dp[1][i]=max(dp[1][i],dp[k][j]+1)
            if(k!=3 and a[2][i]>=a[k][j]):
                dp[2][i]=max(dp[2][i],dp[k][j]+1)
            if(k!=2 and a[3][i]<=a[k][j]):
                dp[3][i]=max(dp[3][i],dp[k][j]+1)
for i in range(0,n):
    for k in range(0,4):
        ans=max(ans,dp[k][i])
print(ans)