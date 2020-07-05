import math
import sys


def execute(s):
    res = 0
    bit = 1
    for a in s[::-1]:
        res += (ord(a) - 64) * bit  # ord函数，返回ASCII值
        bit *= 26
    return res


'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

n = input()
print(execute(n))
