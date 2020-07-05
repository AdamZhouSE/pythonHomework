class edge:
    def __init__(self):
        self.to=0
        self.next=0
        self.data=0
h=[0 for i in range(2005)]
q=[]
e=[edge() for j in range(2005)]
d=[0 for k in range(2005)]
v=[0 for k in range(2005)]
po=0
def bfs(s):
    global d,v,h,q,v
    d = [0 for k in range(2005)]
    v = [0 for o in range(2005)]
    while(len(q)>0):
        q.pop(0)
    q.append(s)
    v[s]=1
    Max=0
    maX=0
    while(len(q)>0):
        x=q[0]
        q.pop(0)
        i=h[x]
        while i>0:
            y=e[i].to
            if(v[y]>0):
                i = e[i].next
                continue
            v[y]=1
            d[y]=d[x]+e[i].data
            q.append(y)
            if(d[y]>Max):
                Max=d[y]
                maX=y
            i=e[i].next
    return maX

def add(x,y,z):
    global po,h
    po=po+1
    e[po].to=y
    e[po].next=h[x]
    h[x]=po
    e[po].data=z
t=list(map(int,input().split(' ')))
n=t[0]
m=t[1]
for i in range(m):
    aaa=list(map(int,input().split(' ')))
    add(aaa[0],aaa[1],aaa[2])
    add(aaa[1],aaa[0],aaa[2])
l=bfs(1)
r=bfs(l)
k=[0 for i in range(2005)]
ans=d[r]
for i in range(1,n+1):
    k[i]=d[i]
bfs(r)
M=0
for i in range(1,n+1):
    M=max(M,min(d[i],k[i]))
print(ans+M)



