def xx(n):
    res=[]
    for i in range(1,n+1):
        res.append(i)
    return res
def delete(g,i):
    res=[]
    for q in range(len(g)):
        if not q==i:
            res.append(g[q])
    return res
nn=int(input())
for p in range(nn):
    a=[int(x) for x in input().split(" ")]
    b=a[0]
    c=a[1]
    d=xx(b)
    k=c-1
    while len(d)>1:
        d=delete(d,k)
        k=(k+c-1)%len(d)
    print(d[0])