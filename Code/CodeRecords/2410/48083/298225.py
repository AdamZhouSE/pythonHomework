arr=input().split(',')
difference = int(input())
n = len(arr)
dp = [1] * n
last_val = {}
max_length = 0
for i in range(n):
    val = arr[i]
    if val - difference in last_val:
        j = last_val[val - difference]
        dp[i] = dp[j] + 1
    last_val[val] = i
    max_length = max(max_length, dp[i])
print(max_length)
