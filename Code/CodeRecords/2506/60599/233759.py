s=input()
count = 1
result = 0
temp = 0
l=list(map(int,s[0:len(s)].split(',')))
nums=l

if not nums:
    print(0)
n, res = len(nums), 1  # 序列长度和初始化最长上升子序列长度
dp = [1] * n  # 初始化 dp
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)  # 更新 dp
    res = max(res, dp[i])  # 更新最长上升子序列长度
print(res)


