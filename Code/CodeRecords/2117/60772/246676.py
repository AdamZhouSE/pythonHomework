import math
import sys

# hundred 3
# thousand 4
# million  7
# billion  10

def execute(n):
    states = []
    for i in range(n):
        states.append(0)

    for i in range(1,n+1):  # n轮
        steps = i
        j = 0
        while j < n:
            j = j + steps - 1
            if j >= n :
                break
            states[j] = 1 - states[j]
            j += 1

    return states.count(1)




Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])

print(execute(n))

