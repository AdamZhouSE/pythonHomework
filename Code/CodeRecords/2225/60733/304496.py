import itertools

n = int(input())
m = int(input())

seen = set()
for cand in itertools.product((0, 1), repeat=4):
    if sum(cand) % 2 == m % 2 and sum(cand) <= m:
        A = []
        for i in range(min(n, 3)):
            light = 1
            light ^= cand[0]
            light ^= cand[1] and i % 2
            light ^= cand[2] and i % 2 == 0
            light ^= cand[3] and i % 3 == 0
            A.append(light)
        seen.add(tuple(A))

res = len(seen)
print(res)
