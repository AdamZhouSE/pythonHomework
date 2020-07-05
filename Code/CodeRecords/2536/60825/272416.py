def findItinerary(tickets):
    from collections import defaultdict
    graph = defaultdict(list)
    res = []
    for x, y in sorted(tickets)[::-1]:
        graph[x].append(y)

    def dfs(tmp):
        while graph[tmp]:
            dfs(graph[tmp].pop())
        res.append(tmp)

    dfs("JFK")
    return res[::-1]

s=input()
s=s.replace('[', ' ')
s=s.replace(']', ' ')
s=s.replace(',', ' ')
s=s.replace('"', ' ')
l=s.split()
edge=[]
for i in range(0, len(l), 2):
    edge.append([l[i], l[i+1]])
print(findItinerary(edge))