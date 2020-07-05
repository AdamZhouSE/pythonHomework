def expand(a):
    b = []
    for r in a:
        b += list(r)
    s = '%d,%d:%s' % (len(a), len(a[0]), ''.join(b))
    return s

import numpy as np

n, m = map(int, input().split())
a = []
for i in range(n):
    a += list(input())
a = np.array(a).reshape(n, m)
d = []
for i in range(n):
    for j in range(m):
        for h in range(1, n - i + 1):
            for w in range(1, m - j + 1):
                s = expand(a[i:i + h, j:j + w])
                if not s in d: d.append(s)
print(len(d))