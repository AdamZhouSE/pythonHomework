# 状态：以arr[x]结尾的最大等差序列为dp  (x, y 是 index, arr[x], arr[y] 是 value，dp[x], dp[y] 是 欲求值)
# 转移: if arr[x] - arr[y] == diff(y < x): dp[x] = max(dp[y] + 1, dp[x])


def func():
    arr = [int(x) for x in input().split(",")]
    diff = int(input())

    dp = [1] * len(arr)

    x = 0
    while x < len(arr):
        y = 0
        while y < x:
            if arr[x] - arr[y] == diff:
                dp[x] = max(dp[x], dp[y] + 1)
            y += 1
        x += 1

    print(max(dp))


func()
