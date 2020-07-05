import math
import sys
import re

'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

x = float(input())
n = int(input())

if n<0:
    x = 1 / x
    n = -n
res = 1.0
for i in range(0,n):
    res = res * x

print(res)


