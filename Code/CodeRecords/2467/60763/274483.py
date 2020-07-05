T = int(input())
for i in range(T):
    mnk = list(map(int, ('' + input()).split(' ')))
    m,n,k = mnk[0],mnk[1],mnk[2]
    a = list(map(int, ('' + input()).split(' ')))
    b = list(map(int, ('' + input()).split(' ')))
    for j in b:
        a.append(j)
    a.sort()
    print(a[k-1])