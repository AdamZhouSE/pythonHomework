import math
import sys

def execute(n):
    count = 10
    for i in range(0,n):
        li = list(str(i))
        if len(li) > 1:
            if len(set(li)) == len(li):
                count += 1
    return count

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])

print(execute(n**10))

