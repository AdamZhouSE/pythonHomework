# 10
def test():
    n = int(input())
    exponents = input().split()
    exponents = list(map(int, exponents))
    graph = [[0] * n for _ in range(0, n)]
    for _ in range(0, n - 1):
        edge = input().split()
        edge = list(map(int, edge))
        graph[edge[0] - 1][edge[1] - 1] = 1
        graph[edge[1] - 1][edge[0] - 1] = 1
    res = fix(graph, exponents)
    print(res,end='')


def fix(graph, exponents):
    res = [sum(exponents)]
    dfs(graph, exponents, res)
    return max(res)


def dfs(graph, exponents, res):
    for i in range(0, len(graph)):
        for j in range(i, len(graph)):
            if graph[i][j] == 1:
                graph[i][j] = 0
                graph[j][i] = 0
                graphs = []
                unions = []
                getUnions(graphs, graph, unions)
                exponents0 = []
                for k in unions[0]:
                    exponents0.append(exponents[k])
                exponents1 = []
                for k in unions[1]:
                    exponents1.append(exponents[k])
                if sum(exponents0) > sum(exponents1):
                    res.append(sum(exponents0))
                    dfs(graphs[0], exponents0, res)
                elif sum(exponents0) < sum(exponents1):
                    res.append(sum(exponents1))
                    dfs(graphs[1], exponents1, res)
                else:
                    res.append(sum(exponents0))
                    dfs(graphs[0], exponents0, res)
                    dfs(graphs[1], exponents1, res)
                graph[i][j] = 1
                graph[j][i] = 1


def getUnions(graphs, graph, unions):
    for i in range(0, len(graph)):
        union = [i]
        for j in range(0, len(graph)):
            if graph[i][j] == 1:
                union.append(j)
        if not unions:
            unions.append(union)
        else:
            ok = False
            for k in range(0, len(unions)):
                if list(set(union).intersection(set(unions[k]))):
                    unions.append(list(set(union).union(set(unions.pop(k)))))
                    ok = True
                    break
            if not ok:
                unions.append(union)
    getFinalUnions(unions)
    for union in unions:
        g = [[0] * len(union) for _ in range(0, len(union))]
        ind = 0
        for i in union:
            oud = 0
            for j in union:
                if graph[i][j] == 1:
                    g[ind][oud] = graph[i][j]
                oud = oud + 1
            ind = ind + 1
        graphs.append(g)
