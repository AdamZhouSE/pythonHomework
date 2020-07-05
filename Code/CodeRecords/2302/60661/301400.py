n,root=map(int,input().split(" "))
fa=[]
lch=[]
rch=[]
for i in range(0,n):
    a,b,c=map(int,input().split(" "))
    fa.append(a)
    lch.append(b)
    rch.append(c)
m=int(input())
l1=[]
l2=[]
for i in range(0,m):
    a,b=map(int,input().split(" "))
    current=a
    aa=[]
    while current!=1:
        aa.append(current)
        if current in lch:
            ind=lch.index(current)
            current=fa[ind]
        elif current in rch:
            ind=rch.index(current)
            current=fa[ind]
    aa.append(1)
    current=b
    while current not in aa:
        if current in lch:
            ind = lch.index(current)
            current = fa[ind]
        elif current in rch:
            ind = rch.index(current)
            current = fa[ind]
    print(current)