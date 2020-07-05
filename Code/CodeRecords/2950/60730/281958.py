s = list(input())
d = 0
dmax = 0
for c in s:
    d += 1 if c == '2' else -1
    if d < 0:
        break
    dmax = max(dmax, d)
print(dmax if d == 0 else -1)
