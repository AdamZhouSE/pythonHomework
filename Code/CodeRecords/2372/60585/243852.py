number=eval(input())
for _ in range(0,number):
    num=input().strip().split(' ')
    num=[int(i) for i in num]
    n=num[0]
    x=num[1]
    y=num[2]
    a=input().strip().split(' ')
    a=[int(i) for i in a]
    b=input().strip().split(' ')
    b=[int(i) for i in b]
    dp=[[0]*(y+1) for _ in range(x+1)]
    for i in range(1,y+1):
        dp[0][i]=dp[0][i-1]+b[i-1]
    for i in range(1,x+1):
        dp[i][0]=dp[i-1][0]+a[i-1]
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i+j<=n:
                dp[i][j]=max(dp[i-1][j]+a[i+j-1],dp[i][j-1]+b[i+j-1])
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp[y][x])