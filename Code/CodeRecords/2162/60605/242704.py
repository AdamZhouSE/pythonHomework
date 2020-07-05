# 题目描述
# 给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。
#
# 返回 N 的长度。如果不存在这样的 N，就返回 -1。

x = eval(input())
n = int(input())

a = abs(n)
res = 1.0
for i in range(n):
    res *= x

if n < 0:
    print('%.5f' % (1.0/res))
else:
    print('%.5f' % res)