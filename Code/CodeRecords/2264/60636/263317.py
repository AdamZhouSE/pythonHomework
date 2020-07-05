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
    tot+=1
    global ver[tot]=y
    global nxt[tot]=head[x]
    global head[x]=tot
def tarjan(x):
    global num+=1
    global dfn[x]=low[x]=num
    global top+=1
    global st[top]=x
    if x==root and head[x]==0:
        global cnt+=1
        global dcc[cnt].append(x)
        return 
    flag=0
    i=head[x]
    while(i):
        y=ver[i]
        if not dfn[y]:
            tarjan(y)
            global low[x]=min(low[x],low[y])
            if low[y]>=dfn[x]:
                flag+=1
                if x!=root or flag>1:
                    global cut[x]=True
                global cnt+=1
                while(True):
                    z=st[top]
                    global top-=1
                    global dcc[cnt].append(z)
                    if(z==y):
                        break
                global dcc[cnt].append(x)
        else:
            global low[x]=min(low[x],dfn[y])
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
        global sta[x]=sta[y]=1
        maxn=max(maxn,max(x,y))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    