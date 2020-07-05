import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.key) + ' connectedTo: ' + str([str(x.key) for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo

    def getId(self):
        return self.key

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

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

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList.keys():
            nv = self.addVertex(f)
        if t not in self.vertList.keys():
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def getCost(self, f, t):
        return self.vertList[f].connectedTo[self.vertList[t]]

    def __iter__(self):
        # 方便迭代遍历
        return iter(self.vertList.values())


def dfs(f: Vertex, t: Vertex, route: list):
    if f == t:
        valid.append(route.copy())
        return
    nbrs = f.getConnections()
    for k, v in nbrs.items():
        if k.key not in route:
            route.append(k.key)
            dfs(k, t, route)
            route.pop()

if __name__ == '__main__':
    '''
    n = 3
    lst = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    '''
    import re

    n = int(input())
    lst = re.findall(r'\[(.*?)\]', input()[1:-1])
    for i in range(len(lst)):
        lst[i] = list(map(int, lst[i].split(',')))
    src = int(input())
    dst = int(input())
    k = int(input())

    g = Graph()
    for i in range(n):
        g.addVertex(i)
    for x in lst:
        g.addEdge(x[0], x[1], x[2])

    valid = []
    dfs(g.getVertex(src), g.getVertex(dst), [src])
    min_cost = sys.maxsize
    for x in valid:
        if len(x)-2 <= k:
            sum_cost = 0
            for i in range(1,len(x)):
                sum_cost+=g.getCost(x[i-1],x[i])
            min_cost = min(min_cost,sum_cost)
    if min_cost == sys.maxsize:
        print(-1)
    else:
        print(min_cost)