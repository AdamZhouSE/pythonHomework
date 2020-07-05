def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    dp = [0] * n
    dp[0] = 10
    for i in range(1,n):
        fi = 9
        for j in range(9,9-i,-1):
            fi *= j
        dp[i] = dp[i-1] + fi
    return dp[-1]
n =int(input())
print(countNumbersWithUniqueDigits(n))