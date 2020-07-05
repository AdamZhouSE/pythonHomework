import math
n = int(input().split('\"')[1])

for m in range(int(math.log(n, 2)), 0, -1):
    lo, hi = 2, int(math.pow(n, 1.0 / m)) + 1
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
