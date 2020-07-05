import math
import sys


def excute(x):
    for i in range(0,x):
        if i*i==x:
            return i
    for i in range(0,x):
        if i*i<x and (i+1)*(i+1)>x:
            return i


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

x = int(Input[0])
print(excute(x))


