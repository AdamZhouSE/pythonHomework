import math
import collections
class edge:
    def sett(self,iddd,uu,vv,jdd):
        self.idd,self.u,self.v,self.jd=iddd,uu,vv,jdd
    def __lt__(self,b):
        return self.v<b.v if(abs(self.jd-b.jd)<1e-10)else self.jd<b.jd
class Pt:
    def sett(self,xx,yy):
        self.x,self.y=xx,yy
    def __sub__(self,b):
        ret=Pt()
        ret.sett(self.x-b.x,self.y-b.y)
        return ret
    def __mul__(self,b):
        return self.x*b.y-self.y*b.x


def lower_bound(nums, target):
    low, high = 0, len(nums)-1
    pos = len(nums)
    while low<high:
        mid = (low+high)//2
        if nums[mid] < target:
            low = mid+1
        else:
            high = mid
    if not nums[low]<target:
        pos = low
    return pos
def gcd(a,b):
    return gcd(b,a%b)if b else a

def add(x,y):
    global tot
    tot+=1
    e[tot].sett(tot,x,y,math.atan2(p[y].y-p[x].y,p[y].x-p[x].x))
    h[x].append(e[tot])
def build():
    global cnt,rt
    for i in range(1,n+1):
        h[i].sort()
    for i in range(2,tot+1):
        v=e[i].v
        kl=lower_bound(h[v],e[i^1])
        if(kl==0):
            kl=len(h[v])
        kl-=1
        nxt[i]=h[v][kl].idd
    for i in range(2,tot+1):
        if(pos[i]):
            continue
        cnt+=1
        pos[i],pos[nxt[i]]=cnt,cnt
        j=nxt[i]
        while(e[j].v!=e[i].u):
            s[cnt]+=(p[e[j].u]-p[e[i].u])*(p[e[j].v]-p[e[i].u])
            j,pos[j]=nxt[j],cnt
        if(s[cnt]<=0):
            rt=cnt
    for i in range(2,tot+1):
        tmp=edge()
        tmp.sett(i,pos[i],pos[i^1],0.0)
        tr[pos[i]].append(tmp)
def dfs(x,las):
    f[x],ss[x]=las,s[x]*s[x]
    s[x]<<=1
    vis[x]=1
    sz=len(tr[x])
    for i in range(sz):
        v=tr[x][i].v
        if(vis[v]):
            continue
        istr[tr[x][i].idd],istr[tr[x][i].idd^1]=1,1
        dfs(v,x)
        s[x]+=s[v]
        ss[x]+=ss[v]
def work():
    global Q,ans1,ans2,n
    qqq=list(map(int,input().split()))
    pr=0
    for _ in range(Q):
        js=(qqq[pr]+ans1)%n+1
        for i in range(1,js+1):
            ask[i]=(qqq[pr+i]+ans1)%n+1
        ask[js+1]=ask[1]
        ans1,ans2=0,0
        for i in range(1,js+1):
            x,y=ask[i],ask[i+1]
            ke=edge()
            ke.sett(0,x,y,math.atan2(p[y].y-p[x].y,p[y].x-p[x].x))
            kl=lower_bound(h[x],ke)
            j=h[x][kl].idd
            if(not istr[j]):
                continue
            if(f[pos[j]]==pos[j^1]):
                ans1+=ss[pos[j]]
                ans2+=s[pos[j]]
            else:
                ans1-=ss[pos[j^1]]
                ans2-=s[pos[j^1]]
        tmp=gcd(ans1,ans2)
        ans1//=tmp
        ans2//=tmp
        print(ans1,ans2)
        pr+=js+1



n,m,Q=map(int,input().split())
N,M,tot,cnt,rt,ans1,ans2=n+5,m*2+5,1,0,0,0,0
e,p=[edge()for i in range(M)],[Pt() for i in range(N)]
h,tr=[[]for i in range(N)],[[]for i in range(M)]
nxt,pos,s,f,ss,vis,istr,ask=[0]*M,[0]*M,[0]*M,[0]*M,[0]*M,[0]*M,[0]*M,[0]*M


for i in range(1,n+1):
    xx,yy=map(int,input().split())
    p[i].sett(xx,yy)
for i in range(1,m+1):
    xx,yy=map(int,input().split())
    add(xx,yy)
    add(yy,xx)
build()
dfs(rt,0)
work()