n = int(input())
a = list(map(int, input().split()))
c, p, m = 1, 0, 0
for i in range(1, n):
    if a[i-1] == a[i]:
        c += 1
    else:
        p = c
        c = 1
    m = max(m, min(p, c))

print(m * 2)
