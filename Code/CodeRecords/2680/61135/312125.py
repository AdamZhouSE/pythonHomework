T=int(input())
def f(row,colum):
    dp=[[0 for i in range(colum)] for j in range(row)]
    for i in range(row):
        dp[i][0]=1
    for i in range(colum):
        dp[0][i]=1
    for i in range(1,row):
        for j in range(1,colum):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return str(dp[row-1][colum-1])
for i in range(0,T):
    nums=input().split(" ")
    nums=list(int(a) for a in nums)
    print(f(nums[0],nums[1]))
