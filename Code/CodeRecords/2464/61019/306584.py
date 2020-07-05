read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

n = read()
ns = read_line()
if not ns:
    print(0)
    exit(0)
s, t, mv = 0, 0, int(1e18)
ttl = 0
while t < len(ns):
    ttl += ns[t]
    t += 1
    if ttl < n:
        continue
    while ttl >= n:
        ttl -= ns[s]
        s += 1
    mv = min(mv, t - s + 1)
print(mv if mv is not int(1e18) else 0)
