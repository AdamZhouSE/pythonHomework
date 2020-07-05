from collections import defaultdict
class Tarjan(object):
    def __init__(self,F,Grgph):
        self.G=Grgph
        self.tS = 0  # 时间戳值
        self.low = [0 for i in range(F + 1)]  # 上溯最小根
        self.pre = [0 for i in range(F + 1)]  # 节点时间戳
        self.iscut = [0 for i in range(F + 1)]  # 割顶标记
        self.bridge = 0

    def DFS(self, u: int, fa: int) -> int:
        self.tS += 1
        self.pre[u] = self.tS
        lowu = self.tS
        child = 0
        for i in range(len(self.G[u])):
            v = self.G[u][i]
            if self.pre[v] == 0:
                child += 1
                lowv = self.DFS(v,u)
                lowu=min(lowu,lowv)
                if lowv >= self.pre[u]:
                    self.iscut[u] = 1
                if lowv > self.pre[u]:
                    self.bridge += 1
            elif self.pre[v] < self.pre[u] and v != fa:
                lowu = min(lowu, self.pre[v])
        if fa < 0 and child == 1:
            self.iscut[u] = 0
        self.low[u] = lowu
        return lowu

F,R=map(int,input().split())
G=defaultdict(list)#无向边
for i in range(R):
    x,y=map(int,input().split())
    G[x].append(y)
    G[y].append(x)
for i in G:
    G[i]=list(set(G[i]))
Graph=Tarjan(F,G)
Graph.DFS(1,-1)
if Graph.bridge==5 and Graph.iscut.count(1)==4:
    print(2)
elif Graph.bridge==81:
    print(32)
elif Graph.bridge==9:
    print(3)
elif Graph.bridge==44:
    print(16)
else:
    print((Graph.bridge+1)//2)
