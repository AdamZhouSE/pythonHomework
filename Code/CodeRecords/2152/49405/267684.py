n = int(input())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
for i in range(n):
    v = [False for j in range(n)]
    ans = 0
    t = i
    while not v[t]:
        ans += a[t]
        v[t] = True
        t = f[t] - 1
    print(ans)