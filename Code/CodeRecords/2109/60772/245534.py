import math
import sys


def execute(n):
    li = list(str(n))
    while len(li) != 1:
        temp = 0
        for item in li:
            temp += int(item)
        li = list(str(temp))
    return int(li[0])


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])
print(execute(n))

