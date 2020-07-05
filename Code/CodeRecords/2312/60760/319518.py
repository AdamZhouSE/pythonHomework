def func(n):
    if n<2:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(n+1):
        for j in range(1,i+1):
            dp[i]+=dp[j-1]*dp[i-j]
    return dp[n]
if __name__ == '__main__':

    n=int(input())
    print(func(n))