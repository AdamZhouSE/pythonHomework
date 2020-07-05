# 7
def test():
    n = int(input())
    graph = [[-1] * n for _ in range(0, n)]
    for _ in range(0, n - 1):
        inp = input().split()
        edge = list(map(int, inp))
        edge[0] = edge[0] - 1
        edge[1] = edge[1] - 1
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    xorRes = [-1] * n
    xorRes[0] = 0
    dfs(0, graph, xorRes)
    m=int(input())
    for _ in range(0,m):
        inp=input().split()
        end1=int(inp[0])-1
        end2=int(inp[1])-1
        print(xorRes[end1]^xorRes[end2])



def dfs(root, graph, xorRes):
    for i in range(0, len(graph)):
        if xorRes[i] == -1 and graph[root][i] != -1:
            xorRes[i] = xorRes[root] ^ graph[root][i]
            dfs(i, graph, xorRes)


test()