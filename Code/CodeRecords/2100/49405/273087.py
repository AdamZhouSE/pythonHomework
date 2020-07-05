def count(n, m):
    s = 0
    t = m
    while n >= t:
        s += n // t
        t *= m
    return s
n = int(input())
print(min(count(n, 2), count(n, 5)))