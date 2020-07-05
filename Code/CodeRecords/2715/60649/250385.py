import collections
s=input()
stones=eval(s)
n=len(stones)
class UnionFind():
    def __init__(self,n):
        self.uf=[-1 for i in range(n)]
        self.sets_count=n
    def find(self,p):
        r=p
        while self.uf[p]>=0:
            p=self.uf[p]
        while r!=p:
            self.uf[r],r=p,self.uf[r]
        return p
    def union(self,p,q):
        pr=self.find(p)
        qr=self.find(q)
        if pr==qr:
            return
        elif self.uf[pr]>self.uf[qr]: #pr的规模更下
            self.uf[qr]+=self.uf[pr]
            self.uf[pr]=qr
        else:
            self.uf[pr]+=self.uf[qr]
            self.uf[qr]=pr
        self.sets_count-=1
u=UnionFind(20000)
for x,y in stones:
    u.union(x,y+10000)
print(n-len({u.find(x) for x,y in stones}))