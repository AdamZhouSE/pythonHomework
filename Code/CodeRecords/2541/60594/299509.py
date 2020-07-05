def findOrder(numCourses, prerequisites):
    clen = len(prerequisites)
    if clen == 0:
        return [i for i in range(numCourses)]
    in_degrees = [0 for _ in range(numCourses)]
    # 邻接表
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
n=int(input())
num=eval(input())
print(findOrder(n,num))