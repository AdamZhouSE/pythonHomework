n,m=map(int,input().split())
fother=[i for i in range(n+1)]
son=[[] for i in range(n+1)]
value=[0]
tmp=list(map(int,input().split()))
value+=tmp
def add(x,a):
    value[x]+=a
    for t in son[x]:
        add(t,a)
for i in range(n-1):
    fr,to=map(int,input().split())
    son[fr].append(to)
    fother[to]=fr
for i in range(m):
    tmp=list(map(int,input().split()))
    if tmp[0]==1:
        x,a=tmp[1],tmp[2]
        value[x]+=a
    elif tmp[0]==2:
        x,a=tmp[1],tmp[2]
        add(x,a)
    else:
        x=tmp[1]
        sum=value[1]
        while x!=1:
            sum+=value[x]
            x=fother[x]
        print(sum)

