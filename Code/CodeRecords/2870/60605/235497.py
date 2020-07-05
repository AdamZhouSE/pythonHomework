# 题目描述
# 现在给定 n 个整数，请使用其中任意个整数（每个只能使用一次），得到一个最大的为偶数的和。
#
# 输入描述
# 第一行为整数的个数 n (1 ≤ n ≤ 100000)
# 第二行为这 n 个整数 (1 ≤ ai ≤ 10^9)
# 输出描述
# 输出一个偶数表示最大的为偶数的和

import collections

n = int(input())
di0 = []
di1 = []
line = input().split()
# print(line)
for i in line:
    num = int(i)
    sign = 1
    if num % 2 == 0: sign = 0
    if sign == 0: di0.append(num)
    else: di1.append(num)

res = sum(di0)
di1 = sorted(di1)
while len(di1) >= 2:
    # print(di1)
    res += di1.pop()
    res += di1.pop()
    # del di1[0]
    # del di1[1]
print(res)

# 8
# 23 76 18 96 45 31 52 15