t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for a in range(1, 2 * n):
        for b in range(1, 2 * n):
            if a * a + b * b <= 4 * n * n:
                res += 1
    print(res)
