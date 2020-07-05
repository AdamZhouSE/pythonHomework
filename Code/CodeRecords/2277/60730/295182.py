def recursive(K, N):
    memo = {}

    def dp(k, n):
        if (k, n) not in memo:
            if n == 0:
                ans = 0
            elif k == 1:
                ans = n
            else:
                lo, hi = 1, n
                while lo + 1 < hi:
                    mi = (lo + hi) / 2
                    t1 = dp(k - 1, mi - 1)
                    t2 = dp(k, n - mi)
                    if t1 < t2:
                        lo = mi
                    elif t1 > t2:
                        hi = mi
                    else:
                        lo = hi = mi
                for mi in range(lo, hi):
                    ans = 1 + min(max(dp(k - 1, mi - 1), dp(k, n - mi)))


k = int(input())
n = int(input())
print(recursive(k, n))

