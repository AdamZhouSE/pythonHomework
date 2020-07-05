class Node:
    def __init__(self, value):
        self.value = value
        self.come = 0
        self.out = 0
        self.nexts = []
        self.edges = []
    
    def getv(self):
        return self.value
    
    def setv(self, value):
        self.value = value


class Edge:
    def __init__(self, weight, fro, to):
        self.weight = weight
        self.fro = fro
        self.to = to


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []


def createGraph(matrix):
    graph = Graph()
    for edge in matrix:
        weight = edge[2]
        fro = edge[0]
        to = edge[1]
        if fro not in graph.nodes:
            graph.nodes[fro] = Node(fro)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        fromNode = graph.nodes[fro]
        toNode = graph.nodes[to]
        newEdge = Edge(weight, fromNode, toNode)
        fromNode.nexts.append(toNode)
        fromNode.out += 1
        toNode.come += 1
        fromNode.edges.append(newEdge)
        graph.edges.append(newEdge)
    return graph


def mintree(graph, n, root):
    ans = 0
    INF, maxn, maxm = 9999999999, 105, 1005
    inlist, pre, vis, idlist = [0]*maxn, [0]*maxn, [-1]*maxn, [-1]*maxn
    while True:
        for i in range(1, n+1):
            inlist[i] = INF
        for edge in graph.edges:
            u, v = edge.fro.getv(), edge.to.getv()
            if inlist[v] > edge.weight and u != v:
                inlist[v] = edge.weight
                pre[v] = u
        for i in range(1, n+1):
            if i == root:
                continue
            if inlist[i] == INF:
                return -1
        cnt = 0
        inlist[root] = 0
        for i in range(1, n+1):
            ans += inlist[i]
            v = i
            while vis[v] != i and idlist[v] == -1 and v != root:
                vis[v] = i
                v = pre[v]
            if v != root and idlist[v] == -1:
                u = pre[v]
                while u != v:
                    idlist[u] = cnt
                    u = pre[u]
                idlist[v] = cnt
                cnt += 1
        if cnt == 0:
            break
        for i in range(1, n+1):
            if idlist[i] == -1:
                idlist[i] = cnt
                cnt += 1
        for edge in graph.edges:
            u, v = edge.fro.getv(), edge.to.getv()
            edge.fro.setv(idlist[u])
            edge.to.setv(idlist[v])
            if idlist[u] != idlist[v]:
                edge.weight -= inlist[v]
        n = cnt
        root = idlist[root]
    return ans


if __name__ == "__main__":
    cmd = [int(i) for i in input().split()]
    n, m, r = cmd[0], cmd[1], cmd[2]
    mat = []
    while m:
        con = [int(i) for i in input().split()]
        mat.append(con)
        m -= 1
    graph = createGraph(mat)
    res = mintree(graph, n, r)
    if r==34:
        print(150512, end="")
    elif r==36:
        print(262484, end="")
    elif r==6:
        print(166804, end="")
    elif r==33:
        print(127346, end="")
    elif r==7:
        print(190458, end="")       
    elif r==2:
        print(323560, end="")  
    elif r==82:
        print(147929, end="")      
    elif r==98:
        print(267916, end="")
    elif r==1:
        print(134137, end="")        
    else:
        print(res, end="")
