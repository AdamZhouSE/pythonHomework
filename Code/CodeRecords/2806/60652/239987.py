n = int(input())
a = []
p = []
for i in range(0, n):
    ai, pi = map(int, input().split())
    a.append(ai)
    p.append(pi)
seg = []
weight = a[0]
price = p[0]
for i in range(1, n):
    if price > p[i]:
        seg.append([weight, price])
        weight = a[i]
        price = p[i]
    else:
        weight += a[i]
seg.append([weight,price])
t = 0
for arr in seg:
    t += arr[0] * arr[1]
print(t)
