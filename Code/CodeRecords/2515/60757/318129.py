nums=list(map(int,input().split(',')))
n=len(nums)
m=int(input())
su=[]
for i in range(n+1):
    su.append(0)
for i in range(1,n+1):
    su[i]=su[i-1]+nums[i-1]
dp=[]
tmp=[]
for i in range(n+1):
    tmp.append(10000)
for j in range(n+1):
    t=tmp[:]
    dp.append(t)
dp[0][0]=0
for i in range(1,m+1):
    for j in range(1,n+1):
        for k in range(i-1,j):
            temp=max(dp[i-1][k],su[j]-su[k])
            dp[i][j]=min(dp[i][j],temp)
print(dp[m][n])            
