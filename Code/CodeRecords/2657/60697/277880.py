tt=list(map(str,input().split(' ')))
t=[]
for i in tt:
    if i!='':
        t.append(int(i))
ress=[]
size=t[0]
opersize=t[1]
parent=[i for i in range(size+1)]
b=[0 for i in range(size+1)]
b[1]=1
def find(x):
    if(b[x]!=1):
        x=find(parent[x])
    return x
def union(p, q):
    parent[p] = q
res=[]
for i in range(size-1):
    ress=list(map(str,input().split(' ')))
    a=[]
    for j in ress:
        if j != '':
            a.append(int(j))
    res.append(a)
    union(res[i][1],res[i][0])
operations=[]
for i in range(opersize):
    operations.append(input().split(' '))
for i in range(opersize):
    opera=operations[i][0]
    num=int(operations[i][1])
    if(opera=='C'):
        b[num]=1
    else:
        y=find(num)
        print(y)