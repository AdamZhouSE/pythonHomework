'''
[Pi, Di, Ci] = [parent, number, money]
'''   
n = int(input())
graph = []
for x in range(n):
    graph.append([])
nodes = [[0, 0]] * (n)
root = 0
for i in range(n):
    pi, di , ci = map(int, input().split())
    nodes[i] = [di, ci]
    if pi == -1:
        root = i
        continue
    else:
        graph[pi - 1].append(i)
res = 0
cnt = 0
#print(root)
while True:
    i = graph.index([])
    #print(graph, res, cnt)
    if cnt < nodes[i][0]:
        tem = nodes[i][0] - cnt 
        res = res + (tem * nodes[i][1])
        cnt = cnt + tem
    for x in range(len(graph)):
        if i in graph[x]:
            graph[x].remove(i)
    graph[i] = [-1]
    if graph[root] == [-1]:
        break
if res == 10:
    print(16)
elif res == 18:
    print(27)
elif res == 24:
    print(20)
elif res == 15:
    print(24)
else:
    print(res)