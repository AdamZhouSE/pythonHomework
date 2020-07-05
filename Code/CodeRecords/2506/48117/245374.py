numStr = input().split(',')
dp = [1] * len(numStr)

if len(numStr) <= 0:
    print(0)
else:
    for i in range(len(numStr)):
        for j in range(i):
            if int(numStr[j]) < int(numStr[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))