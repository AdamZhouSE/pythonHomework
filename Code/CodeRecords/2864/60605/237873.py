# 题目描述
# 给你一个数组 a，里面有 n 个整数。
# 你每次可以选择数组中的一个元素 ak，从数组中删掉它，再删掉所有值等于ak + 1 或者 ak  - 1 的元素，
# 这样你可以得到 ak 分。你可以重复进行多次该操作，请问你最后最多能得多少分？
#
# 输入描述
# 第一行包含一个整数 n (1 ≤ n ≤ 10^5)，表示数字里的元素的个数
# 第二行包含 n 个整数 a1, a2, ..., an (1 ≤ ai ≤ 10^5)
# 输出描述
# 输出一个整数表示你能得到最大分值

import collections

n = int(input())
k = input().strip().split(" ")
li = []
big = -99999
for i in k:
    li.append(int(i))
    big = max(int(i), big)

c = collections.Counter(li)
dp = {}
dp[0] = 0
dp[1] = c[1]
ans=-99999
for i in range(2, big+1):
    dp[i]= max(dp[i-1], dp[i-2]+i*c[i])
    ans = max(ans, dp[i])
if ans == -99999: print("1")
else:print(ans)