T = int(input())
for t in range(T):
    n = int(input())
    m = 2 * n
    a = sum([(2 * i) for i in range(1, n)])
    print(a * m + (m - 1) * m / 2)