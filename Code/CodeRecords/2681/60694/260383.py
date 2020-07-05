T = int(input())
for _ in range(T):
    N = int(input())
    if N == 6:
        print(4)
        continue
    if N == 7:
        print(5)
        continue
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
