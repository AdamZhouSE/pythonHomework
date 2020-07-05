# DFS+欧拉道路
import collections


def findItinerary(tickets):
    graph = collections.defaultdict(list)
    for frm, to in tickets:
        graph[frm].append(to)
    for frm, tos in graph.items():
        tos.sort(reverse=True)
    res = []
    dfs(graph, "JFK", res)
    return res[::-1]


def dfs(graph, source, res):
    while graph[source]:
        v = graph[source].pop()
        dfs(graph, v, res)
    res.append(source)


a = [str(i) for i in input().replace("[", "").replace("]", "").replace("\"", "").replace(",", " ").split(" ")]
while a.count("") != 0:
    a.remove("")
tickets = []
#print(a)
for i in range(0, len(a), 2):
    temp = []
    temp.append(a[i])
    temp.append(a[i + 1])
    tickets.append(temp)
print(findItinerary(tickets))
# print(a)
