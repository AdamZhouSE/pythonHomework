t=int(input())
res=[]
for i in range(3):
    ress=input().split(' ')
    a=[]
    for j in ress:
        if(j!=''):
            a.append(int(j))
    res.append(a)
        
res.append(res[-1])
res.insert(0,[0])
dp=[[0 for i in range(5)] for j in range(t)]
for i in range(1,5):
    dp[0][i]=1
for i in range(1,t):
    for j in range(1,5):
        if(res[j][i-1]<=res[1][i]):
            dp[i][1]=max(dp[i-1][j]+1,dp[i][1])
        if(res[j][i-1]>=res[2][i]):
            dp[i][2]=max(dp[i-1][j]+1,dp[i][2])
        if(j!=3):
            dp[i][3]=max(dp[i-1][j]+1,dp[i][3])
        if (j!= 4):
            dp[i][4] = max(dp[i - 1][j] + 1, dp[i][4])
        if(j==3 and res[j][i-1]<=res[j][i]):
            dp[i][j] = max(dp[i - 1][j] + 1, dp[i][3])
        if(j==4 and res[j][i-1]>=res[j][i]):
            dp[i][j] = max(dp[i - 1][j] + 1, dp[i][4])
maxsize=0
for i in range(1,5):
    maxsize=max(maxsize,dp[t-1][i])
print(maxsize,end='')


