class Vertex():
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}
        self.color = None
        self.pred = None
        self.discovery = None
        self.finish = None
        self.low = None

    def setDiscovery(self, discovery):
        self.discovery = discovery

    def getDiscovery(self):
        return self.discovery

    def setFinish(self, finish):
        self.finish = finish

    def setLow(self,low):
        self.low = low

    def getLow(self):
        return self.low

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPred(self, pred):
        self.pred = pred

    def getPred(self):
        return self.pred

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.key) + ' connectedTo: ' + str([str(x.key) for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo


class TjGraph():
    def __init__(self):
        self.vertList = {}
        self.time = 0
        self.numVertices = 0
        self.scc = []
        self.tjstack = []

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList.keys():
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList.keys():
            self.addVertex(f)
        if t not in self.vertList.keys():
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def tarjan(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.tarjanvisit(aVertex)  # 当这个点没有访问过，就从这个点开始，防止图没走完

    def tarjanvisit(self, startVertex):
        self.tjstack.append(startVertex)  # 进栈
        startVertex.setColor('gray')
        self.time += 1  # 记录进栈顺序（此处用time来维护）
        startVertex.setDiscovery(self.time)  # 记录发现次序（时间戳）
        startVertex.setLow(self.time)  # 记录最小的子树的根
        for nextVertex, weight in startVertex.getConnections().items():
            if startVertex.getPred() != nextVertex:  # 判断是否是pred（防止返回）
                if nextVertex.getColor() == 'white':  # 未被访问过
                    nextVertex.setPred(startVertex)
                    self.tarjanvisit(nextVertex)
                    # 递归出来，通过比较决定startVertex的最小根结点编号
                    startVertex.setLow(min(startVertex.getLow(), nextVertex.getLow()))
                elif nextVertex.getColor() == 'gray':  # 访问过，但还在栈里
                    startVertex.setLow(min(startVertex.getLow(), nextVertex.getDiscovery()))
        if startVertex.getLow() == startVertex.getDiscovery():  # 最小根结点编号与时间戳一致
            parts = []  # 存放强连通子图
            while self.time >= startVertex.getLow():
                v = self.tjstack.pop(-1)
                v.setColor('black')  # 表明出栈，已分类
                parts.append(v)
                self.time -= 1
            self.scc.append(parts)

    def getGroup(self, aVertex):
        for group in self.scc:
            if aVertex in group:
                return group

    def findLeaf(self):
        leaf = 0
        for group in self.scc:
            nbrs = []
            for aVertex in group:
                for k, v in aVertex.getConnections().items():
                    if k not in group:
                        currentGroup = self.getGroup(k)
                        if currentGroup not in nbrs:
                            nbrs.append(currentGroup)
            if len(nbrs) == 1:
                leaf+=1
        return leaf


if __name__ == '__main__':
    f ,r = input().split(' ')
    f, r = int(f), int(r)
    dg = TjGraph()
    for i in range(1, f+1):
        dg.addVertex(i)  
    for i in range(r):
        lst = list(map(int,input().split(' ')))
        dg.addEdge(lst[0], lst[1])

    dg.tarjan()
    print((dg.findLeaf()+1)//2)