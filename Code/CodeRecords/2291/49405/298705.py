n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
for i in range(n - 1):
    ans += a[0] + a[1]
    a = sorted(a[2:] + [a[0] + a[1]])
print(ans)