import math
import sys


def romanToInt(s):
    Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    Int = 0
    for index in range(len(s) - 1):
        if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
            Int -= Roman2Int[s[index]]
        else:
            Int += Roman2Int[s[index]]
    return Int + Roman2Int[s[-1]]


'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''
s = input()
print(romanToInt(s))
