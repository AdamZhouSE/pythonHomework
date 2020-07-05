import math
import sys


def excute(n):
    t = n
    s = ''
    while t > 0:  # 每次循环 是 每次取模得到数字 的过程
        t -= 1  # 把 从1开始满27进位 变回 从0开始满26进位
        a, b = t // 26, t % 26  # 这里b的取值范围是0-25
        s = s + chr(b + 65)  # A的ASCII码是65，b+65表示 0-25 和 A-Z 有了一一对应
        t = a
    return s[::-1]  # 最后将 优先获得的低位数字 反转到最后

'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

n = int(input())
print(excute(n))
