def so(lis,n,m):
    summ=0
    lsumm=0
    for i in lis:
        summ+=i[0]
        lsumm+=i[1]
    if summ<=m:
        return 0
    if lsumm>m:
        return -1
    if lsumm==m:
        return n
    diff = summ-m
    c=[]
    for i in lis:
        c.append(i[0]-i[1])
    for i in range(0,n):
        for j in range(0,n-1):
            if c[j]<c[j+1]:
                temp = c[j]
                c[j]=c[j+1]
                c[j+1]=temp
                temp = lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
    saved = 0
    res=0
    for i in lis:
        saved+=(i[0]-i[1])
        res+=1
        if saved>=diff:
            break
    return res
x=input().split(' ')
n = int(x[0])
m = int(x[1])
lis=[]
for i in range(0,n):
    t= input().split(' ')
    t=list(map(int,t))
    lis.append(t)
print(so(lis,n,m))