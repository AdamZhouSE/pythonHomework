from collections import defaultdict
n = int(input())
list1 = input()[2:-2].split("],[")
list1 = [i.split(',') for i in list1]
list1 = [[int(k) for k in j] for j in list1]
course = defaultdict(list)
indegree = [0 for i in range(n)]
for x, y in list1:
    course[y].append(x)
    course[y].sort()
    indegree[x] += 1
q = []
res = []
for m in range(n):
    if not indegree[m]:
        q.append(m)
while q:
    pre = q.pop()
    res.append(pre)
    for x in course[pre]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)
if len(res) != n:
    res.clear()
print(res)