import math
import sys


def excute(n, m, p):
    states = p // m + 1
    return math.ceil(math.log(n) / math.log(states))


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])
m = int(Input[1])
p  = int(Input[2])

print(excute(n,m,p))
