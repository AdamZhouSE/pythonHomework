f = lambda: map(int, input().split())
n, m, s = f()
wb = [(0, 0)] + list(zip(f(), f()))
t = list(range(n + 1))

def g(x):
    if x == t[x]: return x
    t[x] = g(t[x])
    return t[x]

for i in range(m):
    x, y = f()
    x, y = g(x), g(y)
    if x != y: t[y] = x

p = [[] for j in range(n + 1)]
for i in range(1, n + 1): p[g(i)].append(i)

d = [1] + [0] * s
for q in p:
    if len(q) > 1:
        t = [wb[i] for i in q]
        t.append((sum(x[0] for x in t), sum(x[1] for x in t)))
        t.sort(key=lambda x: x[0])

        for j in range(s, -1, -1):
            if d[j]:
                for w, b in t:
                    if j + w > s: break
                    d[j + w] = max(d[j + w], d[j] + b)

    elif len(q) == 1:
        w, b = wb[q[0]]
        for j in range(s - w, -1, -1):
            if d[j]: d[j + w] = max(d[j + w], d[j] + b)

print(max(d) - 1)