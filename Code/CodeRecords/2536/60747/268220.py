import collections
tickets=eval(input())
def dfs(graph, source, res):
    while graph[source]:
        v = graph[source].pop()
        dfs(graph, v, res)
    res.append(source)
graph = collections.defaultdict(list)
for frm, to in tickets:
    graph[frm].append(to)
for frm, tos in graph.items():
    tos.sort(reverse=True)
res = []
dfs(graph, "JFK", res)
print(res[::-1])