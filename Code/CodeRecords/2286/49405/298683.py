l, m = map(int, input().split())
a = [1 for i in range(l + 1)]
for i in range(m):
    x, y = map(int, input().split())
    a = a[:l] + a[0 for i in range(r - l + 1)] + a[r + 1:]
print(sum(a))