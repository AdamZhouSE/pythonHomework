m = int(input())
n = int(input())
opnum = int(input())
ops = []
for x in range(opnum):
    ops.append(input().split(","))
minx = m
miny = n
for x in ops:
    if int(x[0])<minx:
        minx=int(x[0])
    if int(x[1])<miny:
        miny=int(x[1])
print(minx*miny)
