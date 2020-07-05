def preimageSizeFZF(K):
    def zeta(x):
        return x//5 + zeta(x//5) if x > 0 else 0

    #  k = zeta(x) = int(x/5) + int(x/25) + ... <= x/5 + x/25 + ... = 4x/5 ，
    #  故有 x >= 5K/4 >= K 。x <=5*K+1是个很宽泛的的上界， +1是考虑K=0的情况
    lo, hi = K, 5*K + 1
    while lo < hi:
        mid = (lo + hi) // 2
        r = zeta(mid)
        if r < K: lo = mid + 1
        elif r > K: hi = mid - 1
        else: return 5
    return 0


K = int(input())
print(preimageSizeFZF(K))

