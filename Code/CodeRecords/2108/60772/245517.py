import math
import sys


def execute(n):
    count = 0
    for i in range(0,n+1):
        temp = list(str(i))
        count += temp.count('1')
    return count


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])
print(execute(n))

