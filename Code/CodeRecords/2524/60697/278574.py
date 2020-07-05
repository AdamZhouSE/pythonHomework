class node:
    def __init__(self,x,y):
        self.dat = x
        self.key = y
    def setdatkey(self,x,y):
        self.dat=x
        self.key=y
n=int(input())
N=n+1
a=[node(0,0) for i in range(N)]
fa=[0 for i in range(N)]
dat=[0 for i in range(N)]
son=[[0,0] for i in range(N)]
key=[0 for i in range(N)]
s=[0 for i in range(N)]
top=0
def insert(x,f,p):
    fa[x]=f
    son[f][p]=x
def dfs(x):
    if(x==0):
        return
    print(dat[x],end=' ')
    dfs(son[x][0])
    dfs(son[x][1])

b=list(map(int,input().split(' ')))
b.insert(0,0)
for i in range(1,n+1):
    a[i].setdatkey(x=b[i],y=i)
a.sort(key=lambda x: x.dat)
for i in range(1,n+1):
    last=0
    while(top>0 and key[s[top]]>a[i].key):
        last=top
        top-=1
    dat[i]=a[i].dat
    key[i]=a[i].key
    insert(i,s[top],1)
    insert(s[last],i,0)
    top+=1
    s[top]=i
dfs(son[0][1])




