def numInDictLessThanN(D, N):
    N = str(N)
    n = len(N)
    res = sum(len(D) ** i for i in range(1, n))
    i = 0
    while i < n:
        res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
        if N[i] not in D:
            break
        i += 1
    return res + (i == n)

D = input().split(',')
N = int(input())
print(numInDictLessThanN(D, N))