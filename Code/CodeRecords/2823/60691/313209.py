line = input().split(' ')
n = int(line[0])
k = int(line[1])
dp = []
mod = 1000000007
for i in range(2005):
    dp.append([0]*2005)
for i in range(1,n+1):
    dp[1][i] = 1
for i in range(1,k):
    for j in range(1,n+1):
        for l in range(j,n+1,j):
            dp[i+1][l]+=dp[i][j]
            if dp[i+1][l]>mod:
                dp[i+1][l]-=mod
ans = 0
for i in range(1,n+1):
    ans+=dp[k][i]
    if ans>=mod:
        ans-=mod
print(ans)
