R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
N = R * C
res = []
i, step = 1, 1
while i <= N:
    for j in range(step):
        if 0 <= r0 < R and 0 <= c0 < C:
            res.append([r0, c0])
            i += 1
        c0 += 1
    for j in range(step):
        if 0 <= r0 < R and 0 <= c0 < C:
            res.append([r0, c0])
            i += 1
        r0 += 1
    step += 1
    for j in range(step):
        if 0 <= r0 < R and 0 <= c0 < C:
            res.append([r0, c0])
            i += 1
        c0 -= 1
    for j in range(step):
        if 0 <= r0 < R and 0 <= c0 < C:
            res.append([r0, c0])
            i += 1
        r0 -= 1
    step += 1
print(res)