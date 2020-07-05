n = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
dp = [[0, 0x3f3f3f3f, 0x3f3f3f3f] for x in range(n + 1)]
for j in range(n):
    i = j + 1
    if arr[j] == 0:
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + 1
    if arr[j] == 1:
        dp[i][0] = min(dp[i - 1][0], min(dp[i - 1][1], dp[i - 1][2])) + 1
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
    if arr[j] == 2:
        dp[i][0] = min(dp[i - 1][0], min(dp[i - 1][1], dp[i - 1][2])) + 1
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
    if arr[j] == 3:
        dp[i][0] = min(dp[i - 1][0], min(dp[i - 1][1], dp[i - 1][2])) + 1
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
    
print(min(dp[n][0], dp[n][1], dp[n][2]))
