n=int(input())
sources=[]
for i in range(n):
    x=input()
    sources.append(int(x))
for i in sources:
    res=[]
    for a in range(i,0,-1):
        x=[]
        x.append(a)
        for y in res:
            x.append(y)
        res=x
        for y in range(a):
            z=[]
            z.append(res[-1])
            res.pop(-1)
            for w in res:
                z.append(w)
            res=z
    print(res)