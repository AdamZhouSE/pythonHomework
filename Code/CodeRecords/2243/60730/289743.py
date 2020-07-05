def f(p, q):
    m, n = q, p
    while m & 1 == 0 and n & 1 == 0:
        m, n = m / 2, n / 2
    if m & 1 == 0 and n & 1 == 1:
        return 0
    elif m & 1 == 1 and n & 1 == 1:
        return 1
    elif m & 1 == 1 and n & 1 == 0:
        return 2


p = int(input())
q = int(input())
print(f(p, q))
