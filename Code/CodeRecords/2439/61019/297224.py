import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
info = []
for _ in range(n - 1):
    u, v, w = read_line()
    info.append([u, v, w])

ro = info[-1][0]
v = {ro: info[0][2]}
while info:
    fo = info.pop()
    if fo[0] in v:
        v[fo[1]] = v[fo[0]] ^ fo[2]
    elif fo[1] in v:
        v[fo[0]] = v[fo[1]] ^ fo[2]
    else:
        info.insert(0, fo)

m = read()
for _ in range(m):
    x, y = read_line()
    print(v[x] ^ v[y])
