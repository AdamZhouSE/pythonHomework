R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
res = []
for i in range(R):
    for j in range(C):
        res.append([i, j])
res.sort(key=lambda x: abs((x[0] - r0)) + abs((x[1] - c0)))
print(res)
