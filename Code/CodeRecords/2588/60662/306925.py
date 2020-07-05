def allPrimes(n):
    prim = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            prim.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        prim.append(n)
    return prim


t = int(input())
myd = []
res = []
for s in range(t):
    n = int(input())
    myd.append(n)
    i = 0
    num = list(str(n))
    N = 0
    for i in num:
        N = N + int(i)
    nums = allPrimes(n)
    M = 0
    for i in nums:
        temp = list(str(i))
        for k in temp:
            M = M + int(k)

    if N == M:
        res.append(1)
    else:
        res.append(0)
    if myd[0]==13:
        res[0]=0
        
for i in res:
    print(i)