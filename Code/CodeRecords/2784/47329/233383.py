from collections import Counter
n, m = map(int, input().split())
c = [0] * m
for i in range(m):
    a = list(map(int, input().split()))
    c[i] = a.index(max(a))

c = [c.count(i) for i in range(n)]
print(c.index(max(c)) + 1)
