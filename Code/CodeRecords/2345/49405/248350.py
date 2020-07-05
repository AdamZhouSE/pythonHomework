M = 1 << 30
T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    v = [False for i in range(n + 1)]
    ansa, ansb = M, M
    for m in a:
        if v[m]:
            ansa = min(ansa, m)
        v[m] = True
    for m in range(1, n + 1):
        if not v[m]:
            ansb = min(ansb, m)
    if ansa == M: ansa = 0
    if ansb == M: ansb = 0
    print(str(ansa) + ' ' + str(ansb))