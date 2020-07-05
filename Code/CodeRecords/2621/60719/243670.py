nums = input().split(",")
n = len(nums)
for i in range(n):
    nums[i] = int(nums[i])
dp = [n]
dp[0] = nums[0]
for i in range(1, n):
    dp.append(max(nums[i], nums[i] + dp[i-1]))
res = dp[0]
for i in range(n):
    res = max(res, dp[i])
print(res)


def max(a, b):
    if a >= b:
        return a
    else:
        return b