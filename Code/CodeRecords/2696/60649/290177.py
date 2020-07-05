n=int(input())
a=[]
dp=[[0 for i in range(4)] for i in range(n+1)]
for i in range(3):
    tmp=list(map(int,input().split()))
    tmp=[0]+tmp
    a.append(tmp)
    if i==2:
        a.append(tmp)
dp[1][0]=dp[1][1]=dp[1][2]=dp[1][3]=1
for i in range(2,n+1):
    for j in range(i):
        for k in range(4):
            if a[0][i]>=a[k][j]:
                dp[i][0]=max(dp[i][0],dp[j][k]+1)
            if a[1][i]<=a[k][j]:
                dp[i][1]=max(dp[i][1],dp[j][k]+1)
            if k!=3 and a[2][i]>=a[k][j]:
                dp[i][2]=max(dp[i][2],dp[j][k]+1)
            if k!=2 and a[3][i]<=a[k][j]:
                dp[i][3]=max(dp[i][3],dp[j][k]+1)
res=0
for i in range(1,n+1):
    for k in range(4):
        res=max(res,dp[i][k])
print(res,end="")