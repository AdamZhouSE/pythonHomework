from collections import OrderedDict
t=int(input())
for _ in range(t):
    n, q=map(int, input().split())
    l=list(map(int, input().split()))
    u,r,tr=OrderedDict(), OrderedDict(), OrderedDict()
    for i in range(1,n+1):
        u[i]=1
    a,b=[],[]
    for i in range(0,len(l),2):
        a.append(l[i])
    for i in range(1,len(l),2):
        b.append(l[i])
    del l
    
    for i in range(len(a)):
        if a[i]==1:
            r[b[i]]=1
            del u[b[i]]
        elif a[i]==2:
            tr[b[i]]=1
            del r[b[i]]
        elif a[i]==3:
            tr[b[i]]=1
            del u[b[i]]
        else:
            r[b[i]]=1
            del tr[b[i]]
    if len(u)==0:
        print("EMPTY")
    else:
        for i in u.keys():
            print(i, end=" ")
        print()
    if len(r)==0:
        print("EMPTY")
    else:
        for i in r.keys():
            print(i, end=" ")
        print()
    if len(tr)==0:
        print("EMPTY")
    else:
        for i in tr.keys():
            print(i, end=" ")
        print()