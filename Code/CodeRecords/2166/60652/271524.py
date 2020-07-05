T=int(input())
for sample in range(T):
    n=int(input())
    a=[n]
    while n>1:
        n-=1
        a.insert(0,n)
        index=n
        while index>0:
            a=[a[len(a)-1]]+a[:len(a)-1]
            index-=1
    print(' '.join(str(i) for i in a))