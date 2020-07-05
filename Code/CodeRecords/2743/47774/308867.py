class node:
    def __init__(self):
        self.next=0
        self.to=0
maxn=200010
c=1
a=[node() for i in range(maxn<<1)]
head=[0 for i in range(maxn<<1)]
deep=num=s=ans=[0 for i in range(maxn)]
f=[[0 for i in range(20)] for i in range(maxn)]

def add(x,y):
    global c
    a[c].to=y
    a[c].next=head[x]
    head[x]=c
    c+=1
    a[c].to=x
    a[c].next=head[y]
    head[y]=c
    c+=1
def buildtree(rt):
    i=head[rt]
    while(i!=0):
        will=a[i].to
        if(deep[will]==0):
            deep[will]=deep[rt]+1
            f[will][0]=rt
            buildtree(will)
        i=a[i].next
def step():
    for i in range(1,20):
        for j in range(1,n+1):
            f[j][i]=f[f[j][i-1]][i-1]
def LCA(x,y):
    if(deep[x]<deep[y]):
        t=x
        x=y
        y=t
    for i in range(19,-1,-1):
        if(deep[f[x][i]]>=deep[y]):
	        x=f[x][i]
    if(x==y):
        return x
    for i in range(19,-1,-1):
        if(f[x][i]!=f[y][i]):
            x=f[x][i]
            y=f[y][i]
    return f[x][0]
def work(x,y):
    fa=LCA(x,y)
    s[x]+=1
    s[f[y][0]]+=1
    s[fa]-=1
    if(f[fa][0]!=0):
        s[f[fa][0]]-=1
def getsum(now,rt):
    ans[now]=s[now]
    i=head[now]
    while(i!=0):
        will=a[i].to
        if(will!=rt):
            getsum(will,now)
            ans[now]+=ans[will]
        i=a[i].next

n=int(input())
ss=input().split(' ')
j=0
for i in range(1,n+1):
    num[i]=int(ss[j])
    j+=1
for i in range(1,n):
    x,y=map(int,input().split(' '))
    add(x,y)
    s[i]=deep[i]=0
s[n]=deep[n]=0
deep[1]=1
buildtree(1)
step()
for i in range(1,n):
    work(num[i],num[i+1])
getsum(1,0)
for i in range(1,n+1):
    print(ans[i])
        
        
        
        