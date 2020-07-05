def superEggDrop(K, N):
    def f(x):
        ans = 0
        r = 1
        for i in range(1, K + 1):
            r *= x - i + 1
            r //= i
            ans += r
            if ans >= N: break
        return ans

    lo, hi = 1, N
    while lo < hi:
        mi = (lo + hi) // 2
        if f(mi) < N:
            lo = mi + 1
        else:
            hi = mi
    return lo

K=int(input())
N=int(input())
print(superEggDrop(K, N))