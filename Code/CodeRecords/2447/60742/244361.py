m,n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
res = []
for i in range(n):
    l = [int(i) for i in input().split()]
    res.append(str(min(a[l[0]-1:l[1]])))
print(' '.join(res),end=' ')