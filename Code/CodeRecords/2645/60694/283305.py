import math

piles = eval(input())
H = int(input())
piles.sort()
n = len(piles)
lo, hi = 1, piles[-1]


def eatable(K):
    return sum(math.ceil(p/K) for p in piles) <= H


while lo < hi:
    mi = (lo + hi) // 2
    if not eatable(mi):
        lo = mi + 1
    else:
        hi = mi
print(lo)


