# 并查集

disjointSet = [0]*(1001)
for i in range(1001):
    disjointSet[i] = i
def find(x):
    global disjointSet
    if(disjointSet[x] == x):
        return x
    else:
        disjointSet[x] = find(disjointSet[x])
        return disjointSet[x]

graph = eval(input())
for i in range(0,len(graph)):
    if find(graph[i][0]) == find(graph[i][1]):
        print(graph[i])
        break
    else:
        disjointSet[graph[i][1]] = find(graph[i][0])

