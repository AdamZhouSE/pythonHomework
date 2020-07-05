import queue
N = 100
class E:
    to = 0
    nxt = 0
class Tree:
    head = [0]*N
    cnt = 0
    fa = [[0]*20 for i in range(N)]
    dep = [0]*N
    length = [0]*N
    dl = 0
    dr = 0
    sum = [0]*N
    l = [E() for j in range(N<<1)]
    def Ins(self,x,y):
        self.cnt = self.cnt + 1
        self.l[self.cnt].nxt = self.head[x]
        self.l[self.cnt].to = y
        self.head[x] = self.cnt

    def Dfs(self,x,f):
        self.fa[x][0] = f
        self.dep[x] = self.dep[f] + 1
        for i in range(1,20):
            self.fa[x][i] = self.fa[self.fa[x][i-1]][i-1]
        i = self.head[x]
        while i:
            y = self.l[i].to
            i = self.l[i].nxt
            if y==f :
                continue
            self.Dfs(y,x)

    def Lca(self,x,y):
        if self.dep[x]<self.dep[y]:
            temp = x
            x = y
            y = temp
        for i in range(19,-1,-1):
            f = self.fa[x][i]
            if self.dep[f]>=self.dep[y]:
                x = f
        if x == y: return x

        for i in range(19,-1,-1):
            fx = self.fa[x][i]
            fy = self.fa[y][i]
            if fx != fy:
                x = fx
                y = fy
        return self.fa[x][0]

    def Dis(self,x,y):
        return self.dep[x]+self.dep[y]-2*self.dep[self.Lca(x,y)]

    apr = [0]*N
    dis = [0x3f]*N
    q = queue.Queue()
    def Spfa(self,s):
        self.q.put(s)
        self.dis[s] = 0
        self.apr[s] = 1
        while self.q.qsize():
            x = self.q.get()
            self.apr[x] = 0
            i = self.head[x]
            while i :
                y = self.l[i].to
                i = self.l[i].nxt
                if self.dis[x]+1<self.dis[y]:
                    self.dis[y] = self.dis[x] + 1
                    if not self.apr[y]:
                        self.q.put(y)
                        self.apr[y] = 1
    def sort(self,i,j):
        re = self.length[i:j]
        re.sort()
        for k in range(i,j):
            self.length[k] = re[k-i]

    def Calc(self,n):
        self.Dfs(1,0)
        self.dl = self.dr = 1
        for i in range(1,n+1):
            if self.dep[i]>self.dep[self.dl]:
                self.dl = i
        self.Spfa(self.dl)
        for i in range(1,n+1):
            if self.dis[i]>self.dis[self.dr]:
                self.dr = i
        for i in range(1,n+1):
            self.length[i] = max(self.Dis(i,self.dl),self.Dis(i,self.dr))
        self.sort(1,n+1)
        for i in range(1,n+1):
            self.sum[i] = self.sum[i-1]+self.length[i]
        return self.dis[self.dr]

    def Match(self,n,x):
        l = 1
        r = n
        re = n + 1
        while(l<=r):
            mid = (l+r)>>1
            if self.length[mid]>=x:
                re = mid
                r = mid - 1
            else:l = mid + 1
        return re

tr = []
tr.append(Tree())
tr.append(Tree())

mxd = 0
line = input().split(' ')
n = int(line[0])
m = int(line[1])
for i in range(1,n):
    line = input().split(' ')
    x = int(line[0])
    y = int(line[1])
    tr[0].Ins(y,x)
for i in range(1,m):
    line = input().split(' ')
    x = int(line[0])
    y = int(line[1])
    tr[1].Ins(y, x)
mxd = max(tr[0].Calc(n),tr[1].Calc(m))
ans = 0
for i in range(1,n+1):
    p = tr[1].Match(m,mxd-tr[0].length[i]-1)
    ans +=(p-1)*mxd
    ans += (m-p+1)*tr[0].length[i]+tr[1].sum[m]-tr[1].sum[p-1]+(m-p+1)
print(ans)



