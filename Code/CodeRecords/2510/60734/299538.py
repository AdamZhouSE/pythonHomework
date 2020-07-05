import re
class Vertex:
    def __init__(self, key, weight):
        self.key = key
        self.weight = weight
        self.connectedTo = []

    def addweight(self, add):
        self.weight += add

    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

    def getNeighbors(self):
        return self.connectedTo

    def __str__(self):
        return str(self.key) + ' (' + str(self.weight) + ') ' + 'connectedTo: ' + str([x.key for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key, weight):
        self.numVertices += 1
        newVertex = Vertex(key, weight)
        self.vertList[key] = newVertex

    def addEdge(self, f, t):
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])

    def getVertex(self, key):
        if n in self.vertList:
            return self.vertList[key]
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
        if x not in route:
            route.append(x)
            dfs(x, t, route)
            route.pop()


def bfs(method: int, root: Vertex, target: Vertex, records: list, add: int):
    q = [root]
    records.append(root)
    while q:
        begin = q.pop(0)
        if begin == target:
            if method == 3:
                bfs_add(target, records, add)
                return
            elif method == 4:
                return bfs_sum(target, records)
        records.append(begin)
        nbrs = begin.getNeighbors()
        for x in nbrs:
            if x not in records:
                q.append(x)
                records.append(x)


def bfs_add(target: Vertex, records: list, add):
    q = [target]
    records.append(target)
    while q:
        begin = q.pop(0)
        begin.weight += add
        nbrs = begin.getNeighbors()
        for x in nbrs:
            if x not in records:
                q.append(x)
                records.append(x)


def bfs_sum(target: Vertex, records: list):
    q = [target]
    records.append(target)
    sum = 0
    while q:
        begin = q.pop(0)
        sum += begin.weight
        nbrs = begin.getNeighbors()
        for x in nbrs:
            if x not in records:
                q.append(x)
                records.append(x)
    return sum


if __name__ == '__main__':
    # build graph
    n, m, r, p = input().split(' ')
    n, m, r, p = int(n), int(m), int(r), int(p)
    lst = list(map(int, re.findall(r'\d+',input())))
    g = Graph()
    for i in range(len(lst)):
        g.addVertex(i+1,lst[i])
    for i in range(n-1):
        lst = list(map(int, input().split(' ')))
        g.addEdge(lst[0], lst[1])

    # op
    for i in range(m):
        lst = list(map(int, re.findall(r'\d+',input())))
        if lst[0] == 1:
            valid = []
            dfs(g.getVertex(lst[1]), g.getVertex(lst[2]), [g.getVertex(lst[1])])
            valid = sorted(valid, key=len)
            for v in valid[0]:
                v.addweight(lst[3])
        elif lst[0] == 2:
            valid = []
            dfs(g.getVertex(lst[1]), g.getVertex(lst[2]), [g.getVertex(lst[1])])
            valid = sorted(valid, key=len)
            valid = [x.weight for x in valid[0]]
            print(sum(valid)%p)
        elif lst[0] == 3:
            bfs(lst[0], g.getVertex(r), g.getVertex(lst[1]), [], lst[2])
        elif lst[0] == 4:
            print(bfs(lst[0], g.getVertex(r), g.getVertex(lst[1]), [], 0)%p)