
import math

def addk(vals, x, y, k):
    for i in range(x-1, y):
        vals[i] += k

def avgg(vals, x, y) -> float:
    summ = 0
    for i in range(x-1, y):
        # print(vals[i])
        summ += vals[i]
    # print(summ)
    return summ / (y-x+1)

def factt(vals, x, y) -> float:
    summ = 0
    avggg = avgg(vals, x, y)
    for i in range(x-1, y):
        summ += pow(avggg - vals[i], 2)
    return summ / (y-x+1)

x = input().strip().split()
n = int(x[0])
m = int(x[1])
x = input().strip().split()
vals = []
for i in x:
    vals.append(int(i))
ops = []
for i in range(m):
    ops.append(input())
for i in ops:
    op = i.strip().split()
    if op[0] == "1":
        addk(vals, int(op[1]), int(op[2]), int(op[3]))
    elif op[0] == "2":
        print("%.4f" % avgg(vals, int(op[1]), int(op[2])))
    else:
        print("%.4f" % factt(vals, int(op[1]), int(op[2])))
