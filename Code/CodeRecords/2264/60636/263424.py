N=10000
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
    global num,top,cnt,tot,head,low,dfn,cut,sta,ver,nxt,st,dcc
    head=memset(0)
    low=memset(0)
    dfn=memset(0)
    cut=memset(0)
    sta=memset(0)
    ver=memset(0)
    nxt=memset(0)
    st=memset(0)
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
    global num,top,cnt,tot,root
    num+=1
    dfn[x]=low[x]=num
    top+=1
    st[top]=x
    if x==root and head[x]==0:
        cnt+=1
        dcc[cnt].append(x)
        print(dcc[cnt])
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
    for i in range(m):
        x_y=input().split(" ")
        x=int(x_y[0])
        y=int(x_y[1])
        add(x,y)
        add(y,x)
        sta[x]=sta[y]=1
        maxn=max(maxn,max(x,y))
    res1=0
    res2=1
    for i in range(maxn):
        if not dfn[i] and sta[i]:
            root=i
            tarjan(i)
        elif(sta[i]==0):
            res1+=1
    for i in range(cnt):
        now=0
        for j in range(len(dcc[i])):
            if(cut[dcc[i][j]]):
                now+=1
        if(now>1):
            continue
        elif(now==1):
            res1+=1
            res2*=(len(dcc[i])-1)
        else:
            res1+=2
            res2*=(len(dcc[i])*(len(dcc[i])-1))/2
    print(str(res1))
    print(str(res2))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    