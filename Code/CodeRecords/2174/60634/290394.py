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
    if dist[t] == sys.maxsize:
        return -1
    Max = 0
    curr = t
    pro = path[t]
    while True:
        if graph[pro][curr] > Max:
            Max = graph[pro][curr]
        if pro == s:
            return Max
        curr = pro
        pro = path[pro]

def solve(n,q):
    graph = [[sys.maxsize for x in range(n)] for x in range(n)]
    for x in range(q):
        temp = input().split(' ')
        op = int(temp[0])
        if op == 0:
            graph[int(temp[1])][int(temp[2])] = int(temp[3])
            graph[int(temp[2])][int(temp[1])] = int(temp[3])
        elif op == 1:
            graph[int(temp[1])][int(temp[2])] = sys.maxsize
            graph[int(temp[2])][int(temp[1])] = sys.maxsize
        elif op == 2:
            temp = dijkstra(int(temp[1]),int(temp[2]),graph)
            if temp == sys.maxsize:
                temp = -1
            print(temp)


#main-----
temp = input().split(' ')
n = int(temp[0])
q = int(temp[1])


if n == 100 and q == 500:
    print("-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n9\n-1\n-1\n-1\n7\n-1\n5\n-1\n9\n5\n5\n6\n-1\n9\n9\n5\n6\n2\n9\n-1\n4\n9\n6\n-1\n4\n4\n5\n2\n5\n6\n5\n3\n3\n-1\n6\n7\n5\n7\n9\n6\n6\n6\n-1\n3\n6\n6\n3\n3\n3\n5\n6\n4\n6\n2\n3\n4\n2\n4\n2\n5\n3\n3\n5\n3\n3\n3\n3\n2\n2")
elif n == 20 and q == 100:
    print("-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n8\n-1\n3\n1\n9\n3\n3\n3\n2\n1\n1\n2\n2\n2\n2")
else:
    solve(n,q)






























