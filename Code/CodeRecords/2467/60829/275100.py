n=int(input())
res=[]
for i in range(0,n):
    a=[int(x) for x in str(input()).split(" ")]
    b=[int(x) for x in str(input()).split(" ")]
    c=[int(x) for x in str(input()).split(" ")]
    d=[]
    for i in b:
        if not i in d:
            d.append(i)
    for i in c:
        if not i in d:
            d.append(i)
    d.sort()
    res.append(d[a[2]-1])
for i in range(0,n):
    print(res[i])