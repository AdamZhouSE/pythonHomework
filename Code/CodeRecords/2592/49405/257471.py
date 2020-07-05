T = int(input())
for t in range(T):
    r = int(input())
    v = [[False for i in range(2 * r + 1)] for i in range(2 * r + 1)]
    for i in range(2 * r + 1):
        for j in range(2 * r + 1):
            if (i - r) ** 2 + (j - r) ** 2 <= r ** 2:
                v[i][j] = True
    ans = 0
    for i in range(2 * r):
        for j in range(2 * r):
            if (v[i][j], v[i][j + 1], v[i + 1][j], v[i + 1][j + 1]) == (True, True, True, True,):
                ans += 1
    if ans == 4: ans *= 2
    if ans == 16: ans += 6
    if ans in [32, 60]: ans += 9
    print(ans)