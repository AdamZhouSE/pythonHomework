n=int(input())
sit=list(map(int,input().split()))
dp=[[0]*3 for i in range(n)]
if(sit[0]==1):
    dp[0][2]=1
elif(sit[0]==2):
    dp[0][1]=1
else:
    dp[0][1]=1
    dp[0][2]=1
for i in range(1,n):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    if(sit[i]==0):
        continue
    if(sit[i]==1):
        dp[i][2]=max(dp[i-1][0],dp[i-1][1])+1
    elif(sit[i]==2):
        dp[i][1]=max(dp[i-1][0],dp[i-1][2])+1
    else:
        dp[i][1]=max(dp[i-1][0],dp[i-1][2])+1
        dp[i][2]=max(dp[i-1][0],dp[i-1][1])+1
print(n-max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))