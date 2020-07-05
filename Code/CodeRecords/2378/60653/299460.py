import re
n, m = list([int(n) for n in re.findall(r"\-?\d+", input())])
g = [[0x7f]*100 for i in range(0, 100)]
minn = [0x7f]*100
u = [True]*100
sum = 0
for i in range(0, m):
    a, b, c = list([int(n) for n in re.findall(r"\-?\d+", input())])
    g[b][a] = c
    g[a][b] = c
    sum += c
minn[1] = 0
for i in range(1, n+1):
    k = 0
    for j in range(1, n+1):
        if u[j] and minn[j] < minn[k]:
            k = j
            u[k] = False
    for j in range(1, n+1):
        if u[j] and g[k][j] < minn[j]:
            minn[j] = g[k][j]
total = 0
for i in range(1, n+1):
    total += minn[i]
print(sum-total)