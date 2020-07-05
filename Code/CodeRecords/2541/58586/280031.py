from typing import List, Any, Union

course = int(input())
relation = eval(input())
graph = []
for i in range(course + 1):
    graph.append([])

start = [0] * course
for e in relation:
    start[e[0]] += 1
    graph[e[1]].append(e[0])

root = 0
for i in range(len(start)):
    if start[i] == 0:
        root = i
        break

visited = [0] * (course + 1)
ans = []


def dfs(root: int):
    stack=[root]
    while len(stack)>0:
        current: int=stack.pop()
        if visited[current]:
            return False
        else:
            ans.append(current)
            visited[current]=1
            for i in range(len(graph[current])):
                if not visited[graph[current][i]]:
                    stack.append(graph[current][i])
    return True

if dfs(root):
    print(ans)
else:
    print(-1)
