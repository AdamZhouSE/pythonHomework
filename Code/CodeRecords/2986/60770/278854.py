# https://blog.csdn.net/qq_41823255/article/details/102635069
def solve():
    src=list(input())
    des=list(input())
    l1=len(src)
    l2=len(des)
    dp=[[0 for _ in range(l1+1)] for i in range(l2+1)]

    for i in range(1,l1+1):
        dp[0][i]=i
    for i in range(1,l2+1):
        dp[i][0]=i
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            tmp=(dp[i-1][j-1] if src[j-1]==des[i-1] else dp[i-1][j-1]+1)
            dp[i][j]=min(dp[i][j-1]+1,dp[i-1][j]+1,tmp)
    print(dp[l2][l1])

if  __name__ == '__main__' :
    solve()