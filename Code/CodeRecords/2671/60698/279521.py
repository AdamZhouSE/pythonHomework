def test():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        q = n + 1
        res = 1
        full=int(pow(2,n))
        while n >= q - n:
            res = res + comb(n, q - n)
            n=n-1
        print(full-res)


def comb(n, m):
    s1 = 1
    s2 = 1
    s3 = 1

    for i in range(1, n + 1):
        s1 = s1 * i
    for i in range(1, m + 1):
        s2 = s2 * i
    for i in range(1, n - m + 1):
        s3 = s3 * i
    return s1 // (s2 * s3)


test()


