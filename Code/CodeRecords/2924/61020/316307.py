n, r, avg = map(int, input().split())
a = []
cur = 0
for i in range(n):
    t1, t2 = map(int, input().split())
    cur += t1
    a.append((t2, t1))

a = sorted(a)
ans = 0
avg = avg * n
for i in range(n):
    if cur >= avg:
        break
    need = avg - cur
    temp = min(need, r - a[i][1])
    cur += temp
    ans += temp * a[i][0]


print(ans)

    
