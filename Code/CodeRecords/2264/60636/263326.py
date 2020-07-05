N=1005
head=[]
ver=[]
nxt=[]
low=[]
dfn=[]
st=[]
cut=[]
sta=[]
dcc=[]
top,tot,cnt,num,n,m,root=0,0,0,0,0,0,0
def memset (source):
    global N
    res=[]
    for i in range(N):
        res.append(source)
    return res
def init():
    head=memset(0)
    low=memset(0)
    dfn=memset(0)
    cut=memset(0)
    sta=memset(0)
    num,top,cnt=0,0,0
    dcc=memset([])
    tot=1
def add(x,y):
    global tot
    tot+=1
    ver[tot]=y
    nxt[tot]=head[x]
    head[x]=tot
def tarjan(x):
    num+=1
    dfn[x]=low[x]=num
    top+=1
    st[top]=x
    if x==root and head[x]==0:
        cnt+=1
        dcc[cnt].append(x)
        return 
    flag=0
    i=head[x]
    while(i):
        y=ver[i]
        if not dfn[y]:
            tarjan(y)
            low[x]=min(low[x],low[y])
            if low[y]>=dfn[x]:
                flag+=1
                if x!=root or flag>1:
                    cut[x]=True
                cnt+=1
                while(True):
                    z=st[top]
                    top-=1
                    dcc[cnt].append(z)
                    if(z==y):
                        break
                dcc[cnt].append(x)
        else:
            low[x]=min(low[x],dfn[y])
        i=nxt[i]
while(True):
    m=int(input())
    if m==0:
        break
    init()
    maxn=0
    for i in range(1,m+1):
        x_y=input().split(" ")
        x=int(x_y[0])
        y=int(x_y[1])
        add(x,y)
        add(y,x)
        sta[x]=sta[y]=1
        maxn=max(maxn,max(x,y))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    