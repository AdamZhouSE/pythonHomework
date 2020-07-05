N,M=map(int,input().split())
val=list(map(int,input().split()))
val=[0]+val
child=[[0 for i in range(2)]for i in range(N+1)]
dis=[0 for i in range(N+1)]
fother=dis.copy()
def getf(x):
    while fother[x]!=0:
        x=fother[x]
    return x
def pop(x):
    val[x]=-1
    fother[child[x][0]],fother[child[x][1]]=0,0
    merge(child[x][0],child[x][1])
def merge(x,y):
    if x==0 or y==0:
        return x+y
    if val[x]>val[y] or(val[x]==val[y] and x>y):
        x,y=y,x
    child[x][1]=merge(child[x][1],y)
    fother[child[x][1]]=x
    if dis[child[x][0]]<dis[child[x][1]]:
        child[x][0],child[x][1]=child[x][1],child[x][0]
    dis[x]=dis[child[x][1]]+1
    return x
for i in range(M):
    s=list(map(int,input().split()))
    if s[0]==1:
        x,y=s[1],s[2]
        if val[x]==-1 or val[y]==-1:
            continue
        if x==y:
            continue
        fx,fy=getf(x),getf(y)
        merge(fx,fy)
    else:
        x=s[1]
        if val[x]==-1:
            print(-1)
        else:
            y=getf(x)
            print(val[y])
            pop(y)

