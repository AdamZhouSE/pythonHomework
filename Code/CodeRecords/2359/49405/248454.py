T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ans = -1
    for i in range(n):
        for j in range(i + 1, n):
            ans += a.count(a[i] + a[j])
    if ans == -1: print(ans)
    else: print(ans + 1)