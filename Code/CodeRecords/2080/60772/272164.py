import queue


def bfs(adj, start):
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u,end=" ")
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
    print("")


# graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
# bfs(graph,1)

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
    bfs(graph, begin)
