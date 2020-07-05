n = eval(input())
a = [int(x) for x in input().split()]
res = []
for i in range(n):
    mv, mi = 1e9, 0
    for j in range(i, n):
        if a[j] < mv:
            mv = a[j]
            mi = j
    res.append(mi)
    f = a[i:mi + 1]
    f.reverse()
    a = a[:i] + f + a[mi + 1:]
print(' '.join([str(r + 1) for r in res]), end=' ')
