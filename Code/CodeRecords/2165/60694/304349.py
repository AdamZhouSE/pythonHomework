from collections import defaultdict


def bfs(graph: dict, start):
    ans = []
    visited = set(start)
    q = [start]
    while len(q):
        u = q.pop(0)
        ans.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return ans


graph = defaultdict(list)
T = int(input())
for _ in range(T):
    n, start = input().split()
    n = int(n)
    names = ["-"] + input().split()
    for _ in range(n):
        tmp = input().split()
        for i in range(1, n+1):
            if tmp[i] == '1':
                graph[tmp[0]].append(names[i])


print(*bfs(graph, start))
