n, m = map(int, input().split())
a = [str(i) for i in range(n + 1)]
for i in range(m):
    l, r = map(int, input().split())
    a = a[:l] + list(reversed(a[l:r + 1])) + a[r + 1:]
print(" ".join(a[1:]), end=" ")