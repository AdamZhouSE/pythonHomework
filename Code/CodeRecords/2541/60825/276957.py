def findOrder(numCourses, prerequisites):
    clen = len(prerequisites)
    if clen == 0:
        return [i for i in range(numCourses)]
    in_degrees = [0 for _ in range(numCourses)]
    adj = [set() for _ in range(numCourses)]
    for second, first in prerequisites:
        in_degrees[second] += 1
        adj[first].add(second)

    res = []
    queue = []
    for i in range(numCourses):
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        top = queue.pop(0)
        res.append(top)

        for successor in adj[top]:
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                queue.append(successor)
    if len(res) != numCourses:
        return []
    return res

k=int(input())
s=input()
s=s.replace('[','')
s=s.replace(']','')
l=s.split(',')
l= list(map(int, l))

d=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d.append(dd)

print(findOrder(k,d))