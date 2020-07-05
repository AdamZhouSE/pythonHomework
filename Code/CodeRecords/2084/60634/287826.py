import sys

def dijkstra(s,t,graph):
    dist = graph[s].copy()
    path = [-1 for x in range(len(graph[0]))]
    alFind = [0 for x in range(len(graph[0]))]
    i = 0
    while i < len(graph[s]):
        if graph[s][i] != 0:
            path[i] = s
        i += 1

    alFind[s] = 1
    i = 0
    while i < len(graph[0]):
        min = sys.maxsize
        to = s
        j = 0
        while j < len(dist):
            if alFind[j] != 1 and dist[j] < min:
                min = dist[j]
                to = j
            j += 1

        alFind[to] = 1
        j = 0
        while j < len(dist):
            if alFind[j] != 1 and dist[to] + graph[to][j] < dist[j]:
                dist[j] = dist[to] + graph[to][j]
                path[j] = to
            j += 1
        i += 1
    return dist[t]

#main-----
temp = input().split(' ')
n = int(temp[0])
m = int(temp[1])
s = int(temp[2]) - 1
t = int(temp[3]) - 1

graph = [[sys.maxsize for x in range(n)] for x in range(n)]
for x in range(m):
    temp = input().split(' ')
    a = int(temp[0]) - 1
    b = int(temp[1]) - 1
    right = int(temp[2])
    if right < graph[a][b]:
        graph[a][b] = right
        graph[b][a] = right

print(dijkstra(s,t,graph))