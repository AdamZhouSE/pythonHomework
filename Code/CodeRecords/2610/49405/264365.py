import numpy as np
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(1, n - i + 1):
            if len(np.unique(sorted(a[i:i + j]))) == j:
                ans += j
    print(ans)