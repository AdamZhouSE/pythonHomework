A = eval(input())
res = []
N = len(A)
while N:
    idx = A.index(N)
    res.append(idx + 1)
    A = A[:idx + 1][::-1] + A[idx + 1:]
    res.append(N)
    A = A[:N][::-1] + A[N:]
    N -= 1
while 1 in res:
    res.remove(1)
print(res)