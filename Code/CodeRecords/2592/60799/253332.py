T = int(input())
for ttt in range(T):
    n = int(input())
    d = 2 * n
    d_2 = d * d
    res = 0
    for i in range(1, d):
        for j in range(1, d):
            if i * i + j * j <= d_2:
                res += 1
    print(res)
