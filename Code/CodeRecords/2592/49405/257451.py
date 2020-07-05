T = int(input())
for t in range(T):
    r = int(input())
    v = [[False for i in range(2 * r + 1)] for i in range(2 * r + 1)]
    for i in range(2 * r + 1):
        for j in range(2 * r + 1):
            if (i - r) ** 2 + (j - r) ** 2 <= r ** 2:
                v[i][j] = True
    print(v)