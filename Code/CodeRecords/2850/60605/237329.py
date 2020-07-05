# 题目描述
# Lahub 很无聊，所以他在纸上玩一个游戏：
#
# 在纸上写上 n 个数，只可能是 0 或者 1。他只允许做一次操作：对连续的 k 个数执行 x = 1 - x 的操作。
#
# 请问在执行这样一个操作后，纸上最多能有多少个 1。
#
# 输入描述
# 第一行为纸上的数的个数 n (1 ≤ n ≤ 100)
# 第二行为这 n 个数，0 或者 1
# 输出描述
# 输出一个整数表示进行一次这样的操作后，纸上最多有多少个 1

import re

n = int(input())
x = input().strip().split(" ")
string = ""
size = 0
for i in x:
    if i == "1": size += 1
    string = string + i

li = re.findall("0*", string)
maxlen = 0
for i in li:
    maxlen = max(maxlen, len(i))
print(maxlen+size)