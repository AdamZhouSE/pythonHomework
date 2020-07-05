class Rec:
    def __init__(self):
        self.fr,self.nxt,self.to=0,0,0
def add(x,y):
    cnt+=1
    e[cnt].nxt=head[x]
    e[cnt].fr=x
    e[cnt].to=y
    head[x]=cnt
def tarjan(x,in_edge):
    tot+=1
    dfn[x],low[x],i=tot,tot,head[x]
    while(i):
        if(not dfn[e[i].to]):
            tarjan(e[i].to,i)
            low[x]=min(low[x],low[e[i].to])
            if(dfn[x]<low[e[i].to]):
                bridge[i],bridge[i^1]=1,1
        elif(i!=(in_edge^1)):
            low[x]=min(low[x],dfn[e[i].to])
        i=e[i].nxt
def dfs(x):
    c[x],i=dcc,head[x]
    while(i):
        if(c[e[i].to] or bridge[i]):
            i=e[i].nxt
            continue
        dfs(e[i].to)
        i=e[i].nxt
F,R=map(int,input().split())
mF=F+10
head,headw,dfn,low,c,ans=[0]*mF,[0]*mF,[0]*mF,[0]*mF,[0]*mF,[0]*mF
cnt,cntw,tot,dcc,summ,vis,bridge=1,1,0,0,0,[False]*mF,[False]*(mF<<2)
e,wzc=[Rec() for i in range(mF<<2)],[Rec() for i in range(mF<<2)]

for i in range(1,R+1):
    x,y=map(int,input().split())
    add(x,y)
    add(y,x)
for i in range(1,F+1):
    if(not dfn(i)):
        tarjan(i,0)
for i in range(1,F+1):
    if(not c[i]):
        dcc+=1
        dfs(i)
for i in range(2,cnt+1):
    if(c[e[i].fr]!=c[e[i].to]):
        ans[c[e[i].fr]]+=1
for i in range(1,dcc+1):
    if(ans[i]==1):
        summ+=1
print((summ+1)//2)