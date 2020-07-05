
P = 10007
inv = [0] * P
fac = [0] * P
ifac = [0] * P


def binom(n, m):
    if m > n:
        return 0
    return fac[n] * ifac[m] % P * ifac[n - m] % P


def lucas(n, m):
    if m > n:
        return 0
    if m == 0:
        return 1
    return binom(n % P, m % P) * lucas(n // P, m // P) % P


if __name__ == '__main__':
    inv[1] = 1
    for x in range(2, P):
        inv[x] = -(P // x) * inv[P % x] % P + P
    fac[0] = ifac[0] = 1
    for x in range(1, P):
        fac[x] = fac[x - 1] * x % P
        ifac[x] = ifac[x - 1] * inv[x] % P
    [n, m] = list(map(int, input().split(" ")))
    print(lucas(n * m, n - 1) * inv[n] % P)
