class Vertex:
    def __init__(self,key):
        self.key = key
        self.connectedTo = []

    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

    def __str__(self):
        return str(self.key) + ' connectedTo: ' + str([x.key for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])

    def __iter__(self):
        # 方便迭代遍历
        return iter(self.vertList.values())

    def getVertices(self):
        return self.vertList.values()

def bfs_getheight(root:Vertex):
    q = [root]
    records = [root.key]
    step = 0
    while q:
        ql = len(q)
        for i in range(ql):
            begin = q.pop(0)
            nbrs = begin.getConnections()
            for x in nbrs:
                if x.key not in records:
                    q.append(x)
                    records.append(x.key)
        step+=1
    return step


import re
if __name__ == '__main__':
    n = int(input())
    lst = input()[1:-1]
    lst = re.findall(r'\[(.*?)\]', lst)
    for i in range(len(lst)):
        lst[i] = list(map(int, lst[i].split(',')))
    g = Graph()
    for i in range(n):
        g.addVertex(i)
    for edge in lst:
        g.addEdge(edge[0],edge[1])

    min_h = n
    root = []
    for x in g.getVertices():
        tmp_h = bfs_getheight(x)
        if tmp_h < min_h:
            root.clear()
            root.append(x.key)
            min_h = tmp_h
        elif tmp_h == min_h:
            root.append(x.key)
    print(sorted(root))