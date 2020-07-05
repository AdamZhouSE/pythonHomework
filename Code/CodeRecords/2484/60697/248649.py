t=int(input())
sizes=[]
a=[]
b=[]
for i in range(t):
    sizes.append(list(map(int,input().split(' '))))
    a.append(list(map(int,input().split(' '))))
    b.append(list(map(int,input().split(' '))))
for i in range(t):
    asize= sizes[i][0]
    bsize=sizes[i][1]
    aa=a[i]
    bb=b[i]
    res=[]
    for i in aa:
        if(i not in res):
            res.append(i)
    for j in bb:
        if(j not in res):
            res.append(j)
    print(len(res))

