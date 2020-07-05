a = list(map(int, input().split(",")))
n = len(a)
a = [0] + a
b = [1 for i in range(n + 1)]
ans = 1
for i in range(2, n + 1):
    for j in range(1, i):
        if a[i] > a[j]:
            b[i] = max(b[i], b[j] + 1)
            ans = max(ans, b[i])
print(ans)