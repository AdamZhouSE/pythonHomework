def test():
    t = int(input())
    nmk = input().split()
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])
    sales = input().split()
    sales = list(map(int, sales))
    for i in range(0, len(sales)):
        if sales[i] == 2:
            sales[i] = -1
    routes = []
    for _ in range(0, m):
        route = input().split()
        route = list(map(int, route))
        routes.append(route)
    ab = input().split()
    ab = list(map(int, ab))
    a = ab[0] - 1
    b = ab[1] - 1
    if a == b:
        print(0)
        return
    graph = [[-1] * n for _ in range(0, n)]
    for route in routes:
        begin_index = route[0] - 1
        end_index = route[1] - 1
        time = route[2]
        graph[begin_index][end_index] = time
        graph[end_index][begin_index] = time
    res = []
    route = []
    balance = 0
    findRoute(a, b, balance, k, graph, sales, route, res)
    if res == []:
        print(-1)
    else:
        mintime = -1
        for route in res:
            time = 0
            for i in range(1, len(route)):
                time = time + graph[i - 1][i]
            if mintime == -1:
                mintime = time
            else:
                if mintime > time:
                    mintime = time
        print(mintime)


def findRoute(now, target, balance, k, graph, sales, route, res):
    balance = balance + sales[now]
    if abs(balance) <= k:
        if len(route) >= 2:
            if now == route[-2]:
                return
        copy_route = route
        copy_route.append(now)
        if now == target:
            res.append(copy_route)
            return
        else:
            for i in range(0, len(graph)):
                if graph[now][i] != -1:
                    findRoute(i, target, balance, k, graph, sales, copy_route, res)


test()