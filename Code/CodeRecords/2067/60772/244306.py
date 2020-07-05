import math
import sys
import re


def intToRoman(num):
    # 使用哈希表，按照从大到小顺序排列
    hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}
    res = ''
    for key in hashmap:
        if num // key != 0:
            count = num // key  # 比如输入4000，count 为 4
            res += hashmap[key] * count
            num %= key
    return res


'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''
s = int(input())
print(intToRoman(s))
