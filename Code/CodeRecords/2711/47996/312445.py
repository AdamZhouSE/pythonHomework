def numSimilarGroups(A):
    n = len(A)
    m = len(A[1])
    collect = dict()
    graph = [set() for i in range(n)]
    def similar(s1, s2):
        i, j = -1, -1
        for k in range(len(s1)):
            if s1[k] != s2[k]:
                if i == -1:
                    i = k
                elif j == -1:
                    j = k
                    if s1[i] != s2[j] or s1[j] != s2[i]:
                        return False
                else:
                    return False
        return True
    for i in range(n):
        for j in range(i + 1, n):
            if similar(A[i], A[j]):
                graph[i].add(j)
                graph[j].add(i)
    visited = [0] * n
    res = 0
    def dfs(i, visited, n, graph):
        if visited[i]:
            return
        visited[i] = 1
        for j in graph[i]:
            dfs(j, visited, n, graph)
        return
    for i in range(n):
        if not visited[i]:
            res += 1
            dfs(i, visited, n, graph)
    return res
lst = [x[1:-1] for x in input()[1:-1].split(",")]
print(numSimilarGroups(lst))
