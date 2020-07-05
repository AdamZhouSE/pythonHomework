class treeS:
    def __init__(self):
        global N
        self.c=[0]*N
    def add(self,x,v):
        global n
        while(x<=n):
            self.c[x]+=v
            x+=x&(-x)
    def summ(self,x):
        ans=0
        while(x):
            ans+=self.c[x]
            x-=x&(-x)
        return ans
    def query(self,l,r):
        return 0 if l>r else self.summ(r)-self.summ(l-1)
def dfs(now,nowans):
    global cnt,ans
    if(nowans>=ans):
        return
    if(now>cnt):
        ans=nowans
        return
    up.add(r[now],1)
    dfs(now+1,nowans+min(up.query(l[now],r[now]-1),down.query(l[now],n)+up.query(r[now]+1,n)))
    up.add(r[now],-1)
    down.add(r[now],1)
    dfs(now+1,nowans+min(down.query(l[now],r[now-1]),up.query(l[now],n)+down.query(r[now]+1,n)))
    down.add(r[now],-1)
T=int(input())
for _ in range(T):
    ans,cnt=float('inf'),0
    n=int(input())
    N=n+5
    a,l,r=[0]*N,[0]*N,[0]*N
    up,down=treeS(),treeS()
    a[1:n+1]=map(int,input().split())
    for i in range(1,n+1):
        for j in range(i+2,n+1):
            if(a[i]==a[j]):
                cnt+=1
                l[cnt],r[cnt]=i,j
    dfs(1,0)
    print(ans)