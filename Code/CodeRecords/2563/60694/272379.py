import math
n = int(input())

for m in range(math.log(n, 2), 1, -1):
    lo, hi = 2, math.pow(n, 1.0 / m)
    while lo < hi:
        k_mi = (lo + hi) // 2
        x = sum(k_mi ** i for i in range(m+1))
        if x == n:
            print(k_mi)
            exit()
        elif x < n:
            lo = k_mi + 1
        else:
            hi = k_mi
