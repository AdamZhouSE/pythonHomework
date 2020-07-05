# 题目描述
# 给你一个由 n 个整数组成的数组 a。 你的任务是找到数组中所有元素的公约数的数量。
#
# 例如，如果数组 a 为 [2,4,6,2,10]，则 1 和 2 为这个数组的公约数（因此答案为2）。
#
# 输入描述
# 第一行为数组的长度 n（1≤n≤4⋅10^5）
# 第二行为 n 个整数 (1≤ai≤10^12）
# 输出描述
# 输出一个整数表示数组公约数的数量

import math

n = int(input())
l = input().strip().split(" ")
li = []
for i in l:
    li.append(int(i))

minNum = li[0]
for i in li:
    minNum = min(minNum, i)
cnt = 0
ceil = int(math.sqrt(minNum) // 1)
for i in range(1, ceil+1):
    isOK = True
    for j in li:
        if j % i != 0:
            isOK = False
            break
    if isOK: cnt+=1

print(cnt)