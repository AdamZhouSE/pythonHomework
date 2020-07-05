import re
n = int(input())
ans = 0
f = [0]
d = [0]
mt = [0]
q = []
ind = [0]*1000
now = [0]*1000
for i in range(0, n):
    a, b, c = list([int(n) for n in re.findall(r"\-?\d+", input())])
    f.append(a)
    d.append(b)
    mt.append(c)
    if f[i+1] != -1:
        ind[f[i+1]] += 1
for i in range(0, 100):
    mt.append(0)
for i in range(1, n+1):
    if ind[i] == 0:
        q.append(i)
while len(q) > 0:
    t = q[0]
    if d[t] > now[t]:
        ans += mt[t]*(d[t]-now[t])
    if t != 0:
        mt[f[t]] = min(mt[f[t]], mt[t])
        ind[f[t]] -= 1
        now[f[t]] += max(d[t], now[t])
        if ind[f[t]] == 0:
            q.append(f[t])
    q.remove(q[0])
print(ans)