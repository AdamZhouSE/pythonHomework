import sys
n, d = map(int, input().split(' '))
if d == 0:
    print(1)
else:
    f = []
    f.append(1)
    for i in range(1, d + 1):
        f.append(f[i - 1] ** n + 1)
    print(f[d] - f[d - 1],end='')