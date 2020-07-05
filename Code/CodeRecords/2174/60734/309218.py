import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.distance = sys.maxsize
        self.pred = None
        self.connectedTo = {}

    def addNeighbor(self, nbr, danger):
        self.connectedTo[nbr] = danger

    def deleteNeighbor(self, nbr):
        del self.connectedTo[nbr]

    def getNeighbors(self):
        return self.connectedTo

    def __str__(self):
        return str(self.key) + ' ' + str([str(k) + '(' + str(v) + ')' for k, v in self.connectedTo.items()])

    def getDanger(self, nbr):
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def getPred(self):
        return self.pred

    def setPred(self, pred):
        self.pred = pred


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1

    def getVertex(self, key):
        if key in self.vertList.keys():
            return self.vertList[key]
        else:
            return None

    def addEdge(self, f, t, danger):
        self.vertList[f].addNeighbor(self.vertList[t], danger)
        self.vertList[t].addNeighbor(self.vertList[f], danger)

    def deleteEdge(self, f, t):
        self.vertList[f].deleteNeighbor(self.vertList[t])
        self.vertList[t].deleteNeighbor(self.vertList[f])

    def getDanger(self, f, t):
        return self.vertList[f].connectedTo[self.vertList[t]]

    def __iter__(self):
        # 方便迭代遍历
        return iter(self.vertList.values())

    def getVertices(self):
        return self.vertList.keys()


def dijkstra(g: Graph, start: Vertex, end: Vertex):
    def getShortestPath(target: Vertex):
        path = [target.key]
        current = target
        while current.getPred():
            current = current.getPred()
            path.insert(0, current.key)
        return path
    for x in g:
        x.setDistance(sys.maxsize)
        x.setPred(None)
    start.setDistance(0)
    q = [x for x in g]
    q.sort(key=lambda x: x.getDistance())
    while q:
        currentVex = q.pop(0)
        for k, v in currentVex.getNeighbors().items():
            newDist = currentVex.getDistance() + currentVex.getDanger(k)
            if newDist < k.getDistance():
                k.setDistance(newDist)
                k.setPred(currentVex)
                q.sort(key=lambda x: x.getDistance())

    info = {}.fromkeys(g.getVertices())
    for x in g:
        info[x.key] = [x.getDistance(), getShortestPath(x)]
    return info[end.key][1]


if __name__ == '__main__':
    n, q = input().split(' ')
    n, q = int(n), int(q)

    g = Graph()
    for i in range(n):
        g.addVertex(i)
    for i in range(q):
        lst = list(map(int, input().split(' ')))
        if lst[0] == 0:
            g.addEdge(lst[1], lst[2], lst[3])
        elif lst[0] == 1:
            g.deleteEdge(lst[1], lst[2])
        elif lst[0] == 2:
            path = dijkstra(g, g.getVertex(lst[1]), g.getVertex(lst[2]))

            if len(path) == 1:
                print(-1)
            else:
                max_danger = 0
                for i in range(1, len(path)):
                    tmp = g.getDanger(path[i-1],path[i])
                    max_danger = max(tmp,max_danger)
                print(max_danger)