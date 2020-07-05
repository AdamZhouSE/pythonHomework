k=int(input())


def zeta(x):
    return x / 5 + zeta(x / 5) if x > 0 else 0


lo, hi = k, 10 * k + 1
has=False
while lo < hi:
    mi = (lo + hi) / 2
    zmi = zeta(mi)
    if zmi == k:
        print(5)
        has=True
        break
    elif zmi < k:
        lo = mi + 1
    else:
        hi = mi
if not has:
    print(0)