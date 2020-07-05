def shuzi(A):
    n = len(A)
    if n == 0:
        return 0
    tmp = sum([i * A[i] for i in range(n)])
    res = tmp
    ABCD = sum(A)
    for i in range(n-1):
        tmp = tmp + ABCD - n * A[n-1-i]
        res = max(res, tmp)
    return res
a=input().split(',')
a=[int(x) for x in a]
print(shuzi(a))