import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
dp = [0] * n
orphen = n * (n - 1) // 2
deps = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = read_line()
    deps[x].append(y)
    orphen -= y
queue = [orphen]
ht = 0
while queue:
    for _ in range(len(queue)):
        q = queue.pop(0)
        queue.extend(deps[q])
    ht += 1

print(ht)
