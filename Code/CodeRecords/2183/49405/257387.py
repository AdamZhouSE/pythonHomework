T = int(input())
for t in range(T):
    n = int(input())
    m = 2 * n
    a = (2 + (n - 2) * 2) * (n - 1) + 1
    print(a * m + (m - 1) * m / 2)