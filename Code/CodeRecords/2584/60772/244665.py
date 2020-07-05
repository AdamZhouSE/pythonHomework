import math
import sys


def excute(n):
    return bool(n % 4)


'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

n = int(input())
print(excute(n))

