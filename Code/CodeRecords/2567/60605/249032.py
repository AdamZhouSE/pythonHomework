# 题目描述
# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
# 说明:
# 最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

nums = list(eval(input()))
lower = int(input())
upper = int(input())
cnt = 0

for i in range(len(nums)):
    for j in range(i, len(nums)):
        su = 0
        for k in range(i, j+1):
            su += nums[k]
        if lower <= su <= upper:
            cnt += 1

print(cnt)