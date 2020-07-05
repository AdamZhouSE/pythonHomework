n = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
dp = [[0, 0, 0] for x in range(n + 1)]

for j in range(n):
    i = j + 1
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + 1
    if arr[j] == 1 or arr[j] == 3:
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
    if arr[j] == 2 or arr[j] == 3:
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
print(min(dp[n][0], dp[n][1], dp[n][2]))
