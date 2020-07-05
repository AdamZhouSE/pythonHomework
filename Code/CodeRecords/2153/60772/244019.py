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


li = list(Input[0])
if not(li[0].isdigit()):
    temp = li[1:]
    temp.reverse()
    n = "".join(temp)
    print(-int(n))
else:
    li.reverse()
    n = "".join(li)
    print(int(n))
