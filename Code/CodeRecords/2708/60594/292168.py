num=[int(n) for n in input().split()]
n=num[0]
m=num[1]
q=num[2]
fangjian=[]
yy=[]
zc=[]
for i in range(n):
    zc.append(i+1)
fangjian.append(zc)
for i in range(m-1):
    fangjian.append([])
for i in range(q):
    row=input().split()
    if row[0]=='C':
        ren=int(row[1])
        fj=int(row[2])-1
        for index in range(len(fangjian)):
            if ren in fangjian[index]:
                fangjian[index].remove(ren)
                break
        fangjian[fj].append(ren)
    elif row[0]=='W':
        qishi=int(row[1])-1
        jiehsu=int(row[2])
        final=0
        for index in range(qishi,jiehsu):
            if not fangjian[index] in yy:
                final+=len(fangjian[index])
                zc=fangjian[index].copy()
                yy.append(zc)
        print(final)