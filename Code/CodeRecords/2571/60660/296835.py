n=int(input())
m=[]
for _ in range(n):
    m.append(eval('['+input()+']'))
k=int(input())
dp=[[0 for _ in range(len(m[0])+1)] for _ in  range(n+1)]
for i in range(1,n+1):
    for j in range(1,len(m[0])+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+m[i-1][j-1]
sum=0
res=-99999
for i in range(n):
    for j in range(i+1,n+1):
        for x in range(len(m[0])):
            for y in range(x+1,len(m[0])+1):
                sum=dp[j][y]-dp[j][x]-dp[i][y]+dp[i][x]
                if sum==k:
                    res=k
                    break
                if sum<k:
                    res=max(res,sum)
print(res)