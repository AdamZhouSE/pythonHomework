sizes=list(map(int,input().split(' ')))
n=sizes[0]
k=sizes[1]
dp=[[0 for i in range(n+1)] for j in range(k+1)]
for i in range(n+1):
    dp[1][i]=1
for i in range(1,k):
    for  j in range(1,n+1):
        tmp=int(j**0.5)
        for l in range(1,tmp+1):
            if(j%l==0):
                dp[i+1][j]=dp[i+1][j]+dp[i][l]
                if(l*l!=j):
                    dp[i+1][j]=dp[i+1][j]+dp[i][int(j/l)]
sum=0
for j in range(1,n+1):
    sum=sum+dp[k][j]
print(sum%(10**9+7))