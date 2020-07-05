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
a = int(input())
rev = 0
while a != 0:
    pop = a % 10
    a /= 10
    if rev > 2147483647 / 10 or  (rev == 2147483647 / 10 and pop> 7):
        print(0)
        break
    elif rev < -2147483648 / 10 or (rev == -2147483648 / 10 and pop < -8):
        print(0)
        break
    rev = rev * 10 + pop
print(rev)