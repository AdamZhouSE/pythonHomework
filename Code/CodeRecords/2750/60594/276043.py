def findMinHeightTrees(n, edges):
    from collections import defaultdict
    if not edges:
        return [0]
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    leaves = [i for i in graph if len(graph[i]) == 1]
    while n > 2:
        n -= len(leaves)
        nxt_leaves = []
        for leave in leaves:
            tmp = graph[leave].pop()
            graph[tmp].remove(leave)
            if len(graph[tmp]) == 1:
                nxt_leaves.append(tmp)
        leaves = nxt_leaves
    return list(leaves)
n=int(input())
edges=eval(input())
print(findMinHeightTrees(n,edges))