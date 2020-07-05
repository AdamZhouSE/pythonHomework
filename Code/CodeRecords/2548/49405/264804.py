import numpy as np
for t in range(int(input())):
    s = list(input())
    n = len(s)
    k = int(input())
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if len(np.unique(sorted(list(s[i:j + 1])))) == k:
                ans = max(ans, j - i + 1)
    print(ans)