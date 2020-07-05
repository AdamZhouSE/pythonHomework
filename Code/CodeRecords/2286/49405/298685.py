l, m = map(int, input().split())
a = [1 for i in range(l + 1)]
for i in range(m):
    x, y = map(int, input().split())
    a = a[:x] + [0 for i in range(y - x + 1)] + a[y + 1:]
print(sum(a))