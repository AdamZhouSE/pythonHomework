# 2
def test():
    t = int(input())
    for _ in range(0, t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        graph = [[0] * n for i in range(0, n)]
        for i in range(0, m):
            edge = input().split()
            begin = int(edge[0]) - 1
            end = int(edge[1]) - 1
            graph[begin][end] = 1
            graph[end][begin] = 1
        unions = []
        for i in range(0, n):
            union = [i]
            for j in range(0, n):
                if graph[i][j] == 1:
                    union.append(j)
            if unions == []:
                unions.append(union)
            else:
                ok = False
                for k in range(0, len(unions)):
                    if list(set(union).intersection(set(unions[k]))) != []:
                        unions.append(list(set(union).union(set(unions.pop(k)))))
                        ok = True
                        break
                if not ok:
                    unions.append(union)

        graphs = []
        for union in unions:
            g = [[0] * len(union) for _ in range(0, len(union))]
            ind = 0
            edge = 0
            for i in union:
                oud = 0
                for j in union:
                    if graph[i][j] == 1:
                        g[ind][oud] = graph[i][j]
                        edge = edge + 1
                    oud = oud + 1
                ind = ind + 1
            edge=edge//2
            graphs.append([edge, g])
        ok = True
        for g in graphs:
            if not canColor(g[1], g[0]):
                ok = False
                break
        if ok:
            print('YES')
        else:
            print('NO')


def canColor(graph, edge):
    n = len(graph)
    if existOdd(graph):
        return False
    if edge <= n:
        return True
    elif edge >= n + 2:
        return False
    else:
        delLeaves(graph)
        be=[]
        for i in range(0,len(graph)):
            if graph[i].count(1)==3:
                be.append(i)
        if len(be)!=2:
            print('ERROR')
            return False
        else:
            begin=be[0]
            end=be[1]
            routes_length=[]
            route=[]
            getRoutes(begin,end,graph,route,routes_length)
            if len(routes_length)!=3:
                print('ROUTES_LENGTH ERROR!')
            if routes_length.count(2)==2:
                for i in range(0,len(routes_length)):
                    if routes_length[i]%2!=0:
                        return False
                return True

def getRoutes(begin,end,graph,route,routesl):
    if begin==end:
        routesl.append(len(route))
    else:
        route.append(begin)
        for i in range(0,len(graph)):
            if graph[begin][i]==1:
                if len(route)<2:
                    getRoutes(i,end,graph,list(route),routesl)
                else:
                    if route[-2]!=i:
                        getRoutes(i, end, graph, list(route), routesl)





def delLeaves(graph):
    for i in range(0, len(graph)):
        if graph[i].count(1) <= 1:
            graph.pop(i)
            for g in graph:
                g.pop(i)
            delLeaves(graph)
            break


def existOdd(graph):
    route = []
    res = [False]
    dfs(0, graph, route, res)
    return res[0]


def dfs(inPoint, graph, route, res):
    if res[0]:
        return
    if inPoint in route:
        if len(route) % 2 != 0:
            res[0] = True
    else:
        route.append(inPoint)
        for i in range(0, len(graph)):
            if graph[inPoint][i] == 1 :
                if len(route)<2:
                    dfs(i, graph, list(route), res)
                else:
                    if route[-2]!=i:
                        dfs(i, graph, list(route), res)


test()
