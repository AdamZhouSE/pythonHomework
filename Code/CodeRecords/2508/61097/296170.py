from queue import PriorityQueue

class branch:
    num=0
    app=0
    def __init__(self,num,app):
        self.num=num
        self.app=app
    def __lt__(self,other):
        return self.app<other.app

n,q=input().split()
n=int(n)
q=int(q)
br=[branch(0,0) for i in range(n+1)]
fa=[0 for i in range(n+1)]
son=[0 for i in range(n+1)]
ap=[0 for i in range(n+1)]
for i in range(n-1):
    s,e,a=input().split()
    s=int(s)
    e=int(e)
    a=int(a)
    if(s==1): 
        fa[e]=1
        son[s]+=1
        ap[e]=a
        br[e]=branch(e,a)
    elif fa[s]!=0: 
        fa[e]=s
        son[s]+=1
        br[e]=branch(e,a)
        ap[e]=a
    else: 
        fa[s]=e
        son[e]+=1
        br[s]=branch(s,a)
        ap[s]=a
# print(fa)
# print(son)
# print(br)
pq=PriorityQueue()
for i in range(1,n+1):
    if(son[i]==0): pq.put(br[i])
cut=n-1-q
#print(cut)
while cut>0:
    tmp=pq.get()
    t=tmp.num
    #print(t)
    ap[t]=0
    son[fa[t]]-=1
    if(son[fa[t]]==0): pq.put(br[fa[t]])
    cut-=1
ans=0
for i in range(1,n+1):
    ans+=ap[i]
print(ans)