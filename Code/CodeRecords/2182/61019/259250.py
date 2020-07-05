t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split(' ')]
    init, loc, cnt = [0] * n, 0, 0
    for i in range((n - 1) * k):
        cnt += 1
        while init[loc % n] == 1:
            loc += 1
        if cnt == k:
            init[loc % n] = 1
            cnt = 0
        loc += 1
    for k, v in enumerate(init):
        if v == 0:
            print(k + 1)
            break
