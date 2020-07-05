from collections import defaultdict
class Tarjan(object):
    def __init__(self,F,Grgph):
        self.G=Grgph
        self.tS = 0  # 时间戳值
        self.low = [0 for i in range(F + 1)]  # 上溯最小根
        self.dfn = [0 for i in range(F + 1)]  # 节点时间戳
        self.iscut = [0 for i in range(F + 1)]  # 割顶标记
        self.bridge = 0

    def DFS(self, u: int, fa: int) -> int:
        self.tS += 1
        self.dfn[u] = self.tS
        lowu = self.tS
        child = 0
        for i in range(len(self.G[u])):
            v = self.G[u][i]
            if self.dfn[v] == 0:
                child += 1
                lowv = self.DFS(v,u)
                lowu=min(lowu,lowv)
                if lowv >= self.dfn[u]:
                    self.iscut[u] = 1
                if lowv > self.dfn[u]:
                    self.bridge += 1
            elif self.dfn[v] < self.dfn[u] and v != fa:
                lowu = min(lowu, self.dfn[v])
        if fa < 0 and child == 1:
            self.iscut[u] = 0
        self.low[u] = lowu
        return lowu

while True:
    N=int(input())
    if not N:break
    G=defaultdict(list)
    nodes=set()
    for i in range(N+1):
        z=input()
        if z=='0':break
        x=list(map(int,z.split()))
        nodes.add(x[0])
        for j in range(1,len(x)):
            G[x[j]].append(x[0])
            G[x[0]].append(x[j])
            nodes.add(x[j])
    Graph=Tarjan(len(nodes),G)
    Graph.DFS(1,-1)
    print(Graph.iscut.count(1))