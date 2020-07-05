def find (r):
    a=1
    b=1
    res=[]
    while a*a+b*b<=4*r*r:
        x=[]
        x.append(a)
        x.append(b)
        x.sort()
        if not x in res:
            res.append(x)
    return len(res)
n=int(input())
for i in range(n):
    a=int(input())
    print(fidn(a))