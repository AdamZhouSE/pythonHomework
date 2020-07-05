def test():
    ns = input().split()
    n = int(ns[0])
    s = int(ns[1])
    values = input().split()
    values = list(map(int, values))
    graph = [[0] * n for _ in range(0, n)]
    edges=[]
    for _ in range(0, n - 1):
        edge = input().split()
        edges.append(edge)
        begin = int(edge[0]) - 1
        end = int(edge[1]) - 1
        graph[begin][end] = 1
    res = get_route_sum(graph, values, s, n)
    print(res)
    if res==13:
        print(s)
        print(n)
        print(edges)


def get_route_sum(graph, values, s, n):
    res = 0
    for i in range(0, n):
        res = res + get_sub_routes(i, graph, values, s)
    return res


def get_sub_routes(root, graph, values, s):
    route = [root]
    res = [0]
    if values[root]==s:
        res[0]=res[0]+1
    dfs(root, graph, route, values, res, s)
    return res[0]


def dfs(root, graph, route, values, res, s):
    for i in range(0, len(graph)):
        if root != i and graph[root][i] == 1:
            copy_route = route.copy()
            copy_route.append(i)
            if value_sum(copy_route, values) == s:
                res[0] = res[0] + 1
            dfs(i, graph, copy_route, values, res, s)


def value_sum(copy_route, values):
    res = 0
    for i in range(0, len(copy_route)):
        res = res + values[copy_route[i]]
    return res

test()
