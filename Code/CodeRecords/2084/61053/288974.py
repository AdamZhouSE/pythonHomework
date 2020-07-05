
def minWay(src:int,dest:int,edges:list):
    weights = {}
    weights[src] = 0
    while not dest in weights:
        #选择最短的边
        minWeight = 2**31-1
        i = 0
        newVertice = -1
        while i < len(edges):  
            headAdded = edges[i][0] in weights
            tailAdded = edges[i][1] in weights
            #如果两个端点都可达了就删掉
            if headAdded and tailAdded:
                del edges[i]
                i -= 1
            elif headAdded and not tailAdded:
                if edges[i][2] + weights[edges[i][0]] < minWeight:
                    minWeight = edges[i][2] + weights[edges[i][0]]
                    newVertice = edges[i][1]
            elif not headAdded and tailAdded:
                if edges[i][2] + weights[edges[i][1]] < minWeight:
                    minWeight = edges[i][2] + weights[edges[i][1]]
                    newVertice = edges[i][0]
            i += 1
        if newVertice != -1:
            weights[newVertice] = minWeight
    print(weights[dest])

if __name__ == "__main__":
    n,m,src,dest = map(int,input().split())
    edges = []
    for i in range(m):
        edge = []
        s,t,w = map(int,input().split())
        edge.append(s)
        edge.append(t)
        edge.append(w)
        edges.append(edge)
    minWay(src,dest,edges)