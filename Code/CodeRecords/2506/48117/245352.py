numStr = input().split(',')
dp = [1] * len(numStr)



for i in range(len(numStr)):
    for j in range(len(numStr)):
        if int(numStr[j]) < int(numStr[i]):
            dp[i] = max(dp[i], dp[j] + 1)
if len(numStr) <= 1:
    print(0)
else:
    print(max(dp))

