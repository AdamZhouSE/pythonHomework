from collections import defaultdict


def min_tree(n, edges):
    if len(edges) == 0:
        return [0]
    graph = defaultdict(list)
    # highest height
    to_l = [0] * n
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    # print(graph)
    def dfs(i, visited, depth):
        to_l[i] = max(to_l[i], depth)
        for j in graph[i]:
            if j not in visited:
                dfs(j, visited | {j}, depth + 1)

    leaves = [i for i in graph if len(graph[i]) == 1]
    for i in leaves:
        dfs(i, {i}, 1)
    min_num = min(to_l)
    return [i for i in range(n) if to_l[i] == min_num]


def func():
    n = int(input())
    arr = [[int(y) for y in x.split(", ")] for x in input()[2:-2].split("], [")]
    print(min_tree(n, arr))


func()
