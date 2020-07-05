n = int(input())
edges = list(eval(input()))
graph = {i: [] for i in range(n)}
all_depths = {i: -1 for i in range(n)}
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


def dfs(num, depth, start_node):
    is_visited[num] = 1
    for next_node in graph[num]:
        if is_visited[next_node] == 0:
            dfs(next_node, depth + 1, start_node)
    all_depths[start_node] = max(all_depths[start_node], depth)


is_visited = [0] * n
for start_node in range(n):
    is_visited = [0] * n
    dfs(start_node, 0, start_node)

ans = []
min_val = all_depths[min(all_depths, key=all_depths.get)]
for dep in all_depths:
    if all_depths[dep] == min_val:
        ans.append(dep)

print(str(ans))
