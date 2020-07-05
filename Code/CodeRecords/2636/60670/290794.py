# 总路程=dist(A,B)+max{dist(A,C)+dist(B,C)}
# dist(A,B)是树的直径时最大，然后枚举C求最大值
class edge:
    def __init__(self,cur,to,value,nextedge):
        self.cur=cur
        self.to=to
        self.value=value
        self.nextedge=nextedge

def dfs_dia(x,dist):
    global visited,v,maxdist,side1
    if dist>maxdist:
        maxdist=dist
        side1=x
    head=v[x]
    visited[x]=True
    while head!=None:
        if not visited[head.to]:
            dfs_dia(head.to,dist+head.value)
        head=head.nextedge
    visited[x]=False

def dfs_pre(x,dist):
    global visited,v,dist1
    dist1[x]=dist
    head=v[x]
    visited[x]=True
    while head!=None:
        if not visited[head.to]:
            dfs_pre(head.to,dist+head.value)
        head=head.nextedge
    visited[x]=False

n,m=map(int,input().split())
v=[None for i in range(0,n+1)]
visited=[False for i in range(0,n+1)]
for i in range(0,m):
    info=list(map(int,input().split()))
    newedge=edge(info[0],info[1],info[2],v[info[0]])
    v[info[0]]=newedge
    newedge=edge(info[1],info[0],info[2],v[info[1]])
    v[info[1]]=newedge
# 求树的直径，从任意一点dfs找到最远一点，再从此点dfs找到最远一点，这两个点就是直径两端
# 1-2-3-4
maxdist=0
side1=0
dfs_dia(1,0)
side2=side1
maxdist=0
side1=0
dfs_dia(side2,0)
# 预处理直径端点到其他点的距离
dist1=[0 for i in range(0,n+1)]
dfs_pre(side2,0)
dist2=dist1.copy()
dist1=[0 for i in range(0,n+1)]
dfs_pre(side1,0)
ans=maxdist
for i in range(1,n+1):
    if (i!=side1) and (i!=side2):
        ans=max(ans,maxdist+min(dist1[i],dist2[i]))
print(ans)