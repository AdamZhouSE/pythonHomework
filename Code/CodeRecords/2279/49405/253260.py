T = int(input())
for t in range(T):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    sum = [0 for i in range(n + 1)]
    for i in range(n):
        sum[i + 1] = sum[i] + a[i]
    f = True
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if sum[j] - sum[i - 1] == s and f:
                print('%d %d' % (i, j))
                f = False
    if f: print(-1) 