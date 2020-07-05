def pp(b,i,j):
    d=[]
    for k in range(i,j+1):
        d.append(b[k])
    return d
n=int(input())
for p in range(n):
    a=int(input())
    res=[]
    b=[int(x) for x in input().split(" ")]
    for i in range(0,a-1):
        for j in range(i+1,a):
            c=pp(b,i,j)
            c.sort()
            if not c in res:
                res.append(c)
    print(len(res))