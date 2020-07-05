from fractions import Fraction


def under(x):
    count = best = 0
    i = -1
    for j in range(1, len(m)):
        while m[i + 1] < m[j] * x:
            i += 1
        count += i + 1
        if i >= 0:
            best = max(best, Fraction(m[i], m[j]))
    return count, best


m = list(map(int, eval(input())))
n = int(input())
lo, hi = 0.0, 1.0
while hi - lo > 1e-9:
    mi = (lo + hi) / 2.0
    count, best = under(mi)
    if count < n:
        lo = mi
    else:
        ans = best
        hi = mi
k = []
k.append(ans.numerator)
k.append(ans.denominator)
print(k)
