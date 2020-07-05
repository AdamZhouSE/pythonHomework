arr=list(map(int,input().split(",")))
arr=[1]+arr+[1]
n=len(arr)
dp=[[0]*n for _ in range(n)]
for i in range(n-2,-1,-1):
    for j in range(i+2,n):
        Max=0
        for k in range(i+1,j):
            dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+arr[i]*arr[k]*arr[j])
print(dp[0][-1])