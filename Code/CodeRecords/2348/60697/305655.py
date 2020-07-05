size=list(map(int,input().split(' ')))
n=size[0]
m=size[1]
s=[[""]]
id=[[0 for i in range(105)] for j in range(105)]
ind=0
N=10000
cnt=0
ans=0
mark=[False for i in range(N)]
Flag=[False for i in range(N)]
mat=[0 for i in range(N)]
used=[0 for i in range(N)]
b=[0 for i in range(N)]
p=[0 for i in range(N)]
nextedge=[0 for i in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
class Node:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
e=[Node(0,0) for i in range(N)]
for i in range(1,n+1):
    s.append(" "+input())
    for j in range(1,m+1):
        if(s[i][j]=='.'):
            ind+=1
            id[i][j]=ind
            e[ind]=Node(i,j)
def Add(x,y):
    global cnt,b,nextedge,p
    cnt+=1
    b[cnt]=y
    nextedge[cnt]=p[x]
    p[x]=cnt
def Anode(x,y):
    Add(x,y)
    Add(y,x)
def build_graph():
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(id[i][j]!=0 and ((i+j)&1)!=0):
                for k in range(0,4):
                    xx=i+dx[k]
                    yy=j+dy[k]
                    if(xx==0 or yy==0 or yy>m or xx>n or id[xx][yy]==0):
                        continue
                    Anode(id[i][j],id[xx][yy])
def update(x):
    i=p[x]
    while(i!=0):
        v=b[i]
        if(mat[v]!=0 and Flag[mat[v]]==False):
            Flag[mat[v]]=True
            update(mat[v])
        i=nextedge[i]
def hungary():
    global ans
    for i in range(1,ind+1):
        if((e[i].x+e[i].y)&1)!=0:
            dfs(i,i)
    for i in range(1,ind+1):
        if(mat[i]!=0):
            mat[mat[i]]=i
    for i in range(1,ind+1):
        if(mat[i]==0):
            Flag[i]=True
            update(i)
    for i in range(1,ind+1):
        if(Flag[i]):
            ans+=1
    print(ans)
    for i in range(1,ind+1):
        if(Flag[i]):
            print(e[i].x,e[i].y)
def dfs(x,now):
    i=p[x]
    while (i != 0):
        v = b[i]
        if(used[v]!=now):
            used[v]=now
            if(mat[v]==0 or dfs(mat[v],now)):
                mat[v]=x
                return True

        i = nextedge[i]
    return False
build_graph()
hungary()
