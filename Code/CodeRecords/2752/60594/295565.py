def huilu(matrix,n,i,step,oc):
    matrix[i]=0
    quanwei0=True
    for j in matrix:
        if j!=0:
            quanwei0=False
            break
    if quanwei0:
        oc.append(step)
        return
    find=False
    go=[1,-1,n,-n]
    for j in go:
        if matrix[i+j]!=0:
            find=True
            zc=matrix.copy()
            huilu(zc,n,i+j,step+1,oc)
    if not find:
        return



zc=[]
c=input()
c=input()
while c!="]":
    zc.append(c)
    c=input()
matrix=[]
zc2=[]
for i in zc[0]:
    if i.isdigit():
        zc2.append(int(i))
n=len(zc2)
for i in range(n+2):
    matrix.append(0)
for i in zc:
    matrix.append(0)
    for j in i:
        if j.isdigit():
            matrix.append(int(j))
    matrix.append(0)
for i in range(n+2):
    matrix.append(0)
oc=[]
huilu(matrix,n+2,n+3,0,oc)
if oc==[]:
    print(-1)
else:
    oc.sort()
    print(oc[0])