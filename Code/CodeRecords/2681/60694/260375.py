T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 1
    t = 1
    while t != N:
        if 2 * t <= N:
            t *= 2
            cnt += 1
        else:
            t += 1
            cnt += 1
    print(cnt)
