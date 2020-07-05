'''
给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。
返回 N 的长度。如果不存在这样的 N，就返回 -1。
'''

k = int(input())
if (k % 2 == 0) or (k % 5 == 0):
    print('-1')
else:
    tmp = 1
    len = 1
    while (tmp % k != 0):
        tmp = tmp % k
        tmp = tmp * 10 + 1
        len += 1
    print(len)