import queue


def bfs(adj, start):
    res = []
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        res.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
    return res


test = int(input())
for m in range(test):
    li = input().split()
    n = int(li[0])
    begin = li[1]
    graph = {}
    vertexs = input()
    for i in range(n):
        s = input().split()
        vertex = s[0]  # a
        values = []
        for j in range(i+1, n + 1):
            if s[j] == '1':
                values.append(chr(j + 96))
        graph[vertex] = values
    res = bfs(graph, begin)
    for p in range(len(res)-1):
        print(res[p],end=" ")
    print(res[-1])
