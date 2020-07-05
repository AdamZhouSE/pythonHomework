INF = int(pow(2, 31) - 1)


def test():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    graph = [[INF] * n for _ in range(0, n)]
    for _ in range(0, m):
        edge = input().split()
        start = int(edge[0]) - 1
        end = int(edge[1]) - 1
        weight = int(edge[2])
        graph[start][end] = weight
        graph[end][start] = weight
    nearvex = [-1] * n
    lowcost = [INF] * n
    s = [0] * n
    s[0] = 1
    tree_edge = []
    edge_weight=[]
    for i in range(0, n):
        if graph[0][i] != INF:
            nearvex[i] = 0
            lowcost[i] = graph[0][i]
    for i in range(0, n - 1):
        minimum = INF
        index = -1
        for j in range(0, n):
            if s[j] != 1 and lowcost[j] < minimum:
                minimum = lowcost[j]
                index = j
        s[index] = 1
        tree_edge.append([nearvex[index], index, minimum])
        edge_weight.append(minimum)
        for j in range(0, n):
            if s[j] != 1 and lowcost[j] > graph[index][j]:
                lowcost[j] = graph[index][j]
                nearvex[j] = index
    print(max(edge_weight),end='')
        


test()
