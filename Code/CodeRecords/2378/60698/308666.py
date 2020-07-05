INF = int(pow(2, 31) - 1)


def test():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    graph = [[INF] * n for _ in range(0, n)]
    w_sum = 0
    for _ in range(0, k):
        edge = input().split()
        begin = int(edge[0]) - 1
        end = int(edge[1]) - 1
        weight = int(edge[2])
        w_sum = w_sum - weight
        if weight != 0:
            graph[begin][end] = weight
            graph[end][begin] = weight
    nearvex = [-1] * n
    lowcost = [INF] * n
    s = [0] * n
    s[0] = 1
    span_sum = 0
    tree_edge = []
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
        span_sum = span_sum + minimum
        tree_edge.append([nearvex[index], index, minimum])
        for j in range(0, n):
            if s[j] != 1 and lowcost[j] > graph[index][j]:
                lowcost[j] = graph[index][j]
                nearvex[j] = index
    res = w_sum - span_sum
    print(res)
    
test()
