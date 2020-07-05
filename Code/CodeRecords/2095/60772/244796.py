import math
import sys


def excute(a, b):
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

a = Input[0]
b = Input[1]

print(excute(a, b))
