class Vertex:
    def __init__(self, key):
        self.id = key
        self.sweet = 0
        self.connectedTo = []

    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

    def getNeighbors(self):
        return self.connectedTo

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getsweet(self):
        return self.sweet

    def addsweet(self,plus):
        self.sweet+=plus


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertList[id] = newVertex

    def addEdge(self, f, t):
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])

    def getVertex(self, id):
        if n in self.vertList:
            return self.vertList[id]
        else:
            return None

    def __iter__(self):
        # 方便迭代遍历
        return iter(self.vertList.values())


def dfs(f: Vertex, t: Vertex, route: list):
    if f == t:
        valid.append(route.copy())
        return
    nbrs = f.getNeighbors()
    for x in nbrs:
        if x.id not in route:
            route.append(x.id)
            dfs(x, t, route)
            route.pop()


if __name__ == '__main__':
    n = int(input())
    # n = 5
    lst = list(map(int,input().split(' ')))
    # lst = [1, 4, 5, 3, 2]
    # 加入房间
    g = Graph()
    for i in range(n):
        g.addVertex(i + 1)
    # line = ['1 2', '2 4', '2 3', '4 5']
    for i in range(n - 1):
        f, t = input().split(' ')
        f, t = int(f), int(t)
        g.addEdge(f, t)
    for i in range(1,n):
        valid = []
        dfs(g.getVertex(lst[i-1]), g.getVertex(lst[i]), [lst[i-1]])
        valid = sorted(valid,key=len)
        for v in valid[0][:-1]:
            g.getVertex(v).addsweet(1)
    for i in range(1, n+1):
        print(g.getVertex(i).getsweet())