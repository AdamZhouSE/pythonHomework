R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
res = []
for i in range(R):
    for j in range(C):
        res.append(([i, j], abs(r0 - i) + abs(c0 - j)))
res = sorted(res, key=lambda res: res[1])
res = [v[0] for v in res]
print(res)