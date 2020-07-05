import math
import sys

'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

a = input()
b = input()

index = a.index(".")
num = len(a[index + 1:])

x = float(a)
n = int(b)

print(x**n)
