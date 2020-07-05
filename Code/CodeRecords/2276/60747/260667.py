R=int(input())
C=int(input())
r0=int(input())
c0=int(input())


def nxt(r, c):
    step = 1
    yield (r, c)
    while True:
        for _ in range(step):
            c += 1
            yield (r, c)
        for _ in range(step):
            r += 1
            yield (r, c)
        step += 1
        for _ in range(step):
            c -= 1
            yield (r, c)
        for _ in range(step):
            r -= 1
            yield (r, c)
        step += 1


ans = []
for r, c in nxt(r0, c0):
    if 0 <= r < R and 0 <= c < C:
        ans.append([r, c])
    if len(ans) == R * C:
        break

print(ans)