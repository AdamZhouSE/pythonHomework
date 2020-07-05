n,q=map(int,input().split())
child=[1e10 for i in range(n)]
for _ in range(q):
    get=input().split()
    do=get[0]
    a=int(get[1])
    b=int(get[2])
    if do=='M':
        child[b-1]=a
    if do=='D':
        min_=1e10
        for i in range(b-1,n):
            if child[i]<=a:
                if i+1<min_:
                    min_=i+1
        if min_!=1e10:
            print(min_)
        else:
            print(-1)