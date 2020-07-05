from collections import defaultdict

numCourses = int(input())
prerequisites = eval(input())


graph = defaultdict(list)
degree = [0] * numCourses

for x, y in prerequisites:
    graph[y].append(x)
    degree[x] += 1
res = []
bfs = [i for i in range(numCourses) if degree[i] == 0]
for i in bfs:
    res.append(i)
    for j in graph[i]:
        degree[j] -= 1
        if degree[j] == 0:
            bfs.append(j)

print(res)

 