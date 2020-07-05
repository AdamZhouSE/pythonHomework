from collections import deque
numCourses=eval(input())
prerequisites=eval(input())
indegrees = [0 for _ in range(numCourses)]
adjacency = [[] for _ in range(numCourses)]
queue = deque()
res=[]
for cur, pre in prerequisites:
    indegrees[cur] += 1
    adjacency[pre].append(cur)
for i in range(len(indegrees)):
    if not indegrees[i]: queue.append(i)
while queue:
    pre = queue.popleft()
    res.append(pre)
    numCourses -= 1
    for cur in adjacency[pre]:
        indegrees[cur] -= 1
        if not indegrees[cur]: queue.append(cur)
print(res)
