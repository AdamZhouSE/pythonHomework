def findOrder(numCourses, prerequisites):
    from collections import defaultdict
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
    return res if len(res) == numCourses else []

numCourses = int(input())
str = input()[1:-2].split("],")
if len(str) == 1:
    str[0].replace("]", "")
prerequisites = []
for i in range(len(str)):
    temp = str[i][1:].split(",")
    temp = [int(x) for x in temp]
    prerequisites.append(temp)
print(findOrder(numCourses, prerequisites))
