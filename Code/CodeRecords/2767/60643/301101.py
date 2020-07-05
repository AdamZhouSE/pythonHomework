def  solution(n):
    dp=[0]*(n+1)#dp[i]用来存储对于i解决方法数。
    #基本情况，如果给定的值是0，那么dp[0]=1,表示一种方法
    dp[0]=1
    #逐个考虑给定的3个移动，并在索引大于或等于所选移动的值后更新dp[]表的值
    for i in range(3,n+1):
        dp[i]+=dp[i-3]
    for i in range(5,n+1):
        dp[i]+=dp[i-5]
    for i in range(10,n+1):
        dp[i]+=dp[i-10]
    return dp[n]


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n = int(input())
        ans=solution(n)
        print(ans)