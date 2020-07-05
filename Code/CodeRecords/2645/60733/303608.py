def func(piles, H):

    def possible(K):
        return sum((p - 1) // K + 1 for p in piles) <= H

    lo, hi = 1, max(piles)
    while lo < hi:
        mi = (lo + hi) // 2
        if not possible(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo


piles = list(map(int, input().replace("[", "").replace("]", "").split(",")))
H =int(input())
print(func(piles,H))