s=list(map(int,input().split()))
def add(x):
    sum=value[x]
    for k in son[x]:
        sum+=add(k)
    return sum
cnt=1
while s[0]!=0:
    n,m=s[0],s[1]
    value=[0]
    tmp=list(map(int,input().split()))
    value+=tmp
    father=[i for i in range(n+1)]
    son=[[] for i in range(n+1)]
    edges=[]
    tmp=[]
    total=sum(value)
    for i in range(m):
        fr,to=map(int,input().split())
        if to in tmp: #to点已经有点指向了
            fr,to=to,fr
        tmp.append(to)
        father[to]=fr
        son[fr].append(to)
        edges.append((fr,to))
    min1=1000000000000
    for fr,to in edges:
        sum1=add(to)
        sum2=total-sum1
        sum=abs(sum1-sum2)
        min1=min(min1,sum)
    print("Case",cnt,end="")
    print(":",min1)
    s=list(map(int,input().split()))
    cnt+=1
