def lastOne(n,k):
    a = []
    for i in range(n):
        a.append(i+1)
    i = k
    while len(a)>1:
        if i >=len(a):
            a.remove(a[i%len(a)-1])
        else:
            a.remove(a[i-1])
        i = i%len(a)-1+k
    return a[0]


T = int(input())
for i in range(T):
    nk = (''+input()).split(' ')
    n = int(nk[0])
    k = int(nk[1])
    print(lastOne(n,k))