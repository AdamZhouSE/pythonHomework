n=eval(input())
boys=input().strip().split(' ')
boys=[int(i) for i in boys]
m=eval(input())
girls=input().strip().split(' ')
girls=[int(i) for i in girls]
dp=[[0]*(n+1) for i in range(m+1)]
boys=sorted(boys)
girls=sorted(girls)
for i in range(1,m+1):
    for j in range(1,n+1):
        if abs(boys[j-1]-girls[i-1])<=1:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[m][n])