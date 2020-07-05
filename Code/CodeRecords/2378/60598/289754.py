class UnionFind:
    val = 0
    parent = None

    def __init__(self, x):
        self.val = x

    def find(self):
        if self.parent is None:
            return None
        pa = self.parent
        while pa.parent:
            pa = pa.parent
        return pa

    def union(self, p):
        if self.parent is None:
            self.parent = p
            return
        if not self.is_connect(p):
            pa = p.find()
            if pa is None:
                p.parent = self

    def is_connect(self, p):
        if self == p.find() or p == self.find():
            return True
        if self.find() == p.find() and p.find() is not None:
            return True
        else:
            return False


class Edge:
    weight = 0
    node1 = 0
    node2 = 0

    def __init__(self, f, t, w):
        self.node1 = f
        self.node2 = t
        self.weight = w


def minEdge(edges):
    min = 1000
    index = 0
    for e in range(len(edges)):
        if edges[e].weight < min and not unionSet[edges[e].node1-1].is_connect(unionSet[edges[e].node2-1]):
            min = edges[e].weight
            index = e
    return min, index


line1 = input().split(" ")
N = int(line1[0])
M = int(line1[1])
unionSet = [UnionFind(i) for i in range(N)]
edges = [0 for i in range(M)]
total = 0
for i in range(M):
    temp = input().split(" ")
    one = int(temp[0])
    another = int(temp[1])
    w = int(temp[2])
    total += w
    edges[i] = Edge(one, another, w)

genera = 0
for j in range(N - 1):
    MinEdge = minEdge(edges)
    w = MinEdge[0]
    index = MinEdge[1]
    genera += w
    unionSet[edges[index].node1-1].union(unionSet[edges[index].node2-1])
    edges.remove(edges[index])
print(total - genera,end="")


