def find(a, x):
    if a[x] == x:
        return x
    else:
        a[x] = find(a, a[x])
        return a[x]


s = input()
swap = eval(input())
a = [i for i in range(len(s))]
for x, y in swap:
    a[find(a, y)] = find(a, a[x])
a = [find(a, b) for b in a]

linked = {}
for k, v in enumerate(a):
    if v in linked:
        linked[v].append(k)
    else:
        linked[v] = [k]

res = []
for v in linked.values():
    v.sort()
    t = [s[loc] for loc in v]
    t.sort()
    res += [(v[i], t[i]) for i in range(len(v))]
res.sort()
print(''.join([v for k, v in res]))
