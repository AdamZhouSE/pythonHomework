n = int(input())
P = list(map(int, input().split(",")))
a = [1]
i = 0
while len(a) < 1000000 * 2:
    for p in P:
        a.append(a[i] * p)
    i += 1
import numpy as np
print(np.unique(sorted(a))[n - 1])