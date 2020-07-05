A = [int(x) for x in input().split(',')]
A.sort()
n = len(A)
res = 0
for i in range(n):
    res += A[i] * (2 ** (i) - 2 ** (n - 1 - i))
print(res)
