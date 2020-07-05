num=list(map(int,input().split(",")))
num=[1]+num+[1]
l=len(num)
dp=[[0 for i in range(l)]for i in range(l)]
for r in range(2,l):
    for i in range(0,l-r):
        j=i+r
        for k in range(i+1,j):
            dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+num[i]*num[k]*num[j])
print(dp[0][l-1])