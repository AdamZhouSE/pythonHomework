length = int(input())
array = [[0 for _ in range(4)] for _ in range(length)]
result = [0 for _ in range(length)]
dp = [[0 for _ in range(4)] for _ in range(length)]
for i in range(3):
    temp = input().split()
    for j in range(length):
        array[j][i] = int(temp[j])
for i in range(length):
    array[i][3] = array[i][2]
for i in range(length):
    for j in range(i):
        for k in range(4):
            if array[j][k] <= array[i][0]:
                dp[i][0] = max(dp[i][0], dp[j][k] + 1)
            if array[j][k] >= array[i][1]:
                dp[i][1] = max(dp[i][1], dp[j][k] + 1)
            if array[j][k] >= array[i][2] and k != 3:
                dp[i][2] = max(dp[i][2], dp[j][k] + 1)
            if array[j][k] <= array[i][3] and k != 2:
                dp[i][3] = max(dp[i][3], dp[j][k] + 1)
result = 0
for i in range(4):
    result = max(result, dp[length - 1][i])
print(result + 1, end='')
