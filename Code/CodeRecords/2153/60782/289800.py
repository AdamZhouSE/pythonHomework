"""
题目描述
    给出一个32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""
"""
输入描述
    一个整数
"""
"""
输出描述
    一个整数
"""
x = int(input())
if x >= 0:
    reversed_x = int(str(x)[::-1])
else:
    reversed_x = -int(str(x)[:0:-1])

if -2 ** 31 < reversed_x < 2 ** 31 - 1:
    print(reversed_x)
else:
    print(0)

