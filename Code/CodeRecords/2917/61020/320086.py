n = int(input())
x, y, p = {}, {}, {}
for _ in range(n):
    a, b = map(int, input().split())
    x[a] = x.get(a, 0) + 1
    y[b] = y.get(b, 0) + 1
    p[(a, b)] = p.get((a, b), 0) + 1    
res = 0
for i in x.keys():
    res += x[i] * (x[i]-1) // 2
for i in y.keys():
    res += y[i] * (y[i]-1) // 2
for i in p.keys():
    res -= p[i] * (p[i]-1) // 2
print(res)
