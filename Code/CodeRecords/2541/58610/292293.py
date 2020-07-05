from collections import defaultdict
num_courses = eval(input())
requires = eval(input())
graph = defaultdict(list)
degree = [0] * num_courses
for x, y in requires:
    graph[y].append(x)
    degree[x] += 1
res = []
bfs = [i for i in range(num_courses) if degree[i] == 0]
for i in bfs:
    res.append(i)
    for j in graph[i]:
        degree[j] -= 1
        if degree[j] == 0:
            bfs.append(j)
print(res if len(res) == num_courses else [])