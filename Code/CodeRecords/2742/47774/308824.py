import random
class op:
    def __init__(self):
        self.l=0
        self.r=0
        self.size=0
        self.rnd=0
        self.v=0
t=[op() for i in range(50*5005)]
cnt=0
rt=[0 for i in range(5005)]
def update(k):
    t[k].size=t[t[k].l].size+t[t[k].r].size+1
def newnode(k,x):
    global cnt
    cnt+=1
    k=cnt
    t[k].v=x
    t[k].size=1
    t[k].rnd=random.random()
def merge(a,b):
    global cnt
    if(a==0 or b==0):
        return a+b
    if(t[a].rnd>t[b].rnd):
        cnt+=1
        p=cnt
        t[p]=t[a]
        t[p].r=merge(t[p].r,b)
        update(p)
        return p
    else:
        cnt+=1
        p=cnt
        t[p]=t[b]
        t[p].l=merge(a,t[p].l)
        update(p)
        return p
def split(now,k,x,y):
    global cnt
    if(now==0):
        x,y=0,0
    else:
        if(t[now].v<=k):
            cnt+=1
            x=cnt
            t[x]=t[now]
            split(t[x].r,k,t[x].r,y)
            update(x)
        else:
            cnt+=1
            y=cnt
            t[y]=t[now]
            split(t[y].l,k,x,t[y].l)
            update(y)
def Delete(root,w):
    x,y,z=0,0,0
    split(root,w,x,z)
    split(x,w-1,x,y)
    y=merge(t[y].l,t[y].r)
    root=merge(merge(x,y),z)
def Insert(root,w):
    x,y,z=0,0,0
    split(root,w,x,y)
    newnode(z,w)
    root=merge(merge(x,z),y)
def getval(k,w):
    if(w==t[t[k].l].size+1):
        return t[k].v
    elif(w<=t[t[k].l].size):
        return getval(t[k].l,w)
    else:
        return getval(t[k].r,w-t[t[k].l].size-1)
def getkth(root,w):
    x,y=0,0
    split(root,w-1,x,y)
    ans=t[x].size+1
    root=merge(x,y)
    return ans
def getpre(root,w):
    x,y,k,ans=0,0,0,0
    split(root,w-1,x,y);
    if(x==0):
        return -9999
    k=t[x].size
    ans=getval(x,k)
    root=merge(x,y)
    return ans
def getnex(root,w):
    x,y,ans=0,0,0
    split(root,w,x,y);
    if(y==0):
        return 9999
    else:
        ans=getval(y,1)
    root=merge(x,y)
    return ans
n=int(input())
for i in range(1,n+1):
    tim,f,w=map(int,input().split(' '))
    rt[i]=rt[tim];
    if(f==1):
        Insert(rt[i],w)
    elif(f==2):
        Delete(rt[i],w)
    elif(f==3):
        print(getkth(rt[i],w))
    elif(f==4):
        print(getval(rt[i],w))
    elif(f==5):
        print(getpre(rt[i],w))
    else:
        print(getnex(rt[i],w))