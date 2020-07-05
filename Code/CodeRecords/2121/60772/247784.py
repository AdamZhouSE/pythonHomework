import math
import sys

def execute(n):
    if not n:
        return 1
    res, muls = 10, 9
    for i in range(1, min(n, 10)):
        muls *= 10 - i
        res += muls
    return res

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])

print(execute(n))

