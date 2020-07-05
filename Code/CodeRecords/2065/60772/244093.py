import math
import sys
import re


def myAtoi(str):
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    str = str.lstrip()  # 清除左边多余的空格
    num_re = re.compile(r'^[\+\-]?\d+')  # 设置正则规则
    num = num_re.findall(str)  # 查找匹配的内容
    num = int(*num)  # 由于返回的是个列表，解包并且转换成整数
    return max(min(num, INT_MAX), INT_MIN)  # 返回值


'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''
s = input()
print(myAtoi(s))
