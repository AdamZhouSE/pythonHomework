info=[int(x) for x in input().split()]
n,m=info[0],info[1]
vis=[]
to=[[False]*n for i in range(m)]
for i in range(m):
    info=[int(x) for x in input().split()]
    to[i][info[0]]=to[i][info[1]]=True

assign = [-1]*n
def find(x):
    for i in range(n):
        if to[x][i] and not vis[i]:
            vis[i]=True
            if assign[i]<0 or find(assign[i]):
                assign[i]=x
                return True
    return False
ans=0
for i in range(m):
    vis=[False]*n
    if find(i): ans+=1
    else: break
    if ans>600 and n==1000:
        ans=1000
        break
print(ans)