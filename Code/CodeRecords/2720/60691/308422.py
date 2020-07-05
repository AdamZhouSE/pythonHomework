N = eval(input())
temp = input()[2:-2].split("],[")
graph = {}
for x in range(N):
    graph[x] = []

edges = []
for te in temp:
    te = list(map(int,te.split(",")))
    edges.append(te)

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

zero = 0
cnt = 0
points = list(graph.keys())
for point in points:
    if(len(graph[point]) == 0 ):
        zero += 1
    elif(len(graph[point]) > 1):
        for epoint in graph[point]: # 如何放置无节点
            if(len(graph[point]) == 1):
                break
            if(len(graph[epoint]) > 2):
                graph[point].remove(epoint)
                graph[epoint].remove(point)
                cnt += 1
cnt += 1
for point in points:
    if(len(graph[point]) == 1):
        cnt -= 1
        break
if(cnt >= zero):
    print(zero)
else:
    print(-1)
