T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    lm = [0 for i in range(n)]
    rm = [0 for i in range(n)]
    lm[0] = a[0]
    rm[n - 1] = a[n - 1]
    for i in range(1, n):
        lm[i] = max(lm[i - 1], a[i])
    for i in range(n - 2, -1, -1):
        rm[i] = min(rm[i + 1], a[i])
    ans = -1
    for i in range(1, n - 1):
        if lm[i] <= a[i] and a[i] <= rm[i]:
            ans = a[i]
            break
    print(ans)