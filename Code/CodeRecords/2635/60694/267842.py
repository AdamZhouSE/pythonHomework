def preimageSizeFZF(K):
    def zeta(x):
        return x//5 + zeta(x//5) if x > 0 else 0
    
    lo, hi = K, 10*K + 1
    while lo < hi:
        mid = (lo + hi) // 2
        zmi = zeta(mid)
        if zmi < K: lo = mid + 1
        elif zmi > K: hi = mid - 1
        else: return 5
    return 0


K = int(input())
print(preimageSizeFZF(K))

