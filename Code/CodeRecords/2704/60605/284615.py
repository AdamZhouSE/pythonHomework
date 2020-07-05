def isTree(liOfPaths: [[int]], node: int):
    visited = [False for i in range(node)]
    curr = 0
    visited[0] = True
    dfs(visited, curr, liOfPaths)
    for i in visited:
        if not i: return False
    return True

def dfs(visited: [], curr: int, liOfPaths: [[int]]):
    for i in liOfPaths[curr]:
        if not visited[i]:
            visited[i] = True
            dfs(visited, i, liOfPaths)

if __name__ == '__main__':
    graph = list(eval(input()))
    n = len(graph)
    liOfPaths = [[] for i in range(n)]
    for i in graph:
        i[0] -= 1
        i[1] -= 1
        liOfPaths[i[0]].append(i[1])
        liOfPaths[i[1]].append(i[0])
    # print(graph)
    able = -1
    for i in range(len(graph)):
        # newGraph = graph[0:able] + graph[able + 1:]
        liOfPaths[graph[i][0]].remove(graph[i][1])
        liOfPaths[graph[i][1]].remove(graph[i][0])
        if isTree(liOfPaths, n):
            able = i
        liOfPaths[graph[i][0]].append(graph[i][1])
        liOfPaths[graph[i][1]].append(graph[i][0])

    graph[able][0] += 1
    graph[able][1] += 1
    print(graph[able])