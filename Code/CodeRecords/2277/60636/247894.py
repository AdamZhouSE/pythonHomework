def superEggDrop(k,n):
    dp=[]
    for i in range(n+1):
        dps=[]
        for j in range(k+1):
            dps.append(0)
        dp.append(dps)
        for i in range(1, k + 1):
            for step in range(1, n + 1):
                dp[i][step] = dp[i - 1][step - 1] + (dp[i][step - 1] + 1)
                if dp[k][step] >= n:
                    return step
        return 0

k=int(input())
n=int(input())
print(superEggDrop(k,n))