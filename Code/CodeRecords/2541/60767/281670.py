
def ans(indegrees,adjacency):
    queue = []
    res = []
    for t in getZeroIndegree(indegrees,visited):
        queue.append(t)
    while(len(queue)!=0):
        temp = queue.pop(0)
        if(temp in res):
            return []
        for x in range(len(adjacency[temp])):
            indegrees[adjacency[temp][x]] -= 1
        res.append(temp)
        for t in getZeroIndegree(indegrees,visited):
            queue.append(t)
    return res


def getZeroIndegree(indegrees,visited):
    res = []
    for i in range(len(indegrees)):
        if(indegrees[i]==0 and visited[i]!=1):
            res.append(i)
            visited[i]=1
    return res
n = int(input())
indegrees = [0]*n #记录每个节点的入度
adjacency = [[] for i in range(n)] #记录每个节点的领接节点
visited = [0]*n #赋值查找入度为零的节点
tmp = eval(input())
for t in tmp:
    indegrees[int(t[0])] += 1
    adjacency[int(t[1])].append(int(t[0]))
print(ans(indegrees,adjacency))
