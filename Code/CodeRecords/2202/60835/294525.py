for i in range(int(input())):
    n = int(input())
    def ways(n):
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        tile = [1,2]
        for i in range(2,n+1):
            for j in tile:
                dp[i]+=dp[i-j]
        print(dp[n])
    ways(n)