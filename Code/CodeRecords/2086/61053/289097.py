def findParent(i,disjset:list):
    while disjset[i] != -1:
        i = disjset[i]
    return i

def union(i,j,disjset:list):
    disjset[findParent(i,disjset)] = j

def minimalSpanningTree(nodes,edges):
    edges = sorted(edges,key=lambda e:e[2])
    disjset = []
    totalWeight = 0
    count = 0
    for i in range(nodes):
        disjset.append(-1)
    for i in range(len(edges)):
        if findParent(edges[i][0]-1,disjset) != findParent(edges[i][1]-1,disjset):
            union(edges[i][0]-1,edges[i][1]-1,disjset)
            totalWeight += edges[i][2]
            count += 1
        #边数等于节点数-1
        if count == nodes-1:
            break
    print(totalWeight,end="")

if __name__ == "__main__":
    n,m = map(int,input().split(" "))
    edge = []
    for i in range(m):
        newedge = list(map(int,input().split(" ")))
        edge.append(newedge)
    minimalSpanningTree(n,edge)