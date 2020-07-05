n = int(input())
course = []
s = str(input()).strip('[]').split(',')
classFor = []
for j in s:
    course.append(int(j.strip('[]')))

for i in range(0, len(course) - 1):
    temp = []
    if i % 2 == 0:
        temp.append(course[i])
        temp.append(course[i + 1])
        classFor.append(temp)

res = []
fake = []
graph = [[0] for i in range(n)]
degree = [0 for i in range(n)]

if not classFor:
    print([i for i in range(n)])
indegree = [0 for _ in range(n)]
adj = [set() for _ in range(n)]

for end, start in classFor:
    indegree[end] += 1
    adj[start].add(end)

from collections import deque

queue = deque()
for i, x in enumerate(indegree):
    if not x:
        queue.append(i)
res = []
while queue:
    cur = queue.popleft()
    res.append(cur)

    for neighbor in adj[cur]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
if len(res) == n:
    print(res)
else:
    print('[]')