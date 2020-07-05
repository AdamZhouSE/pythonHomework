# 从叶节点开始 每次去除一层叶节点

def findMinHeightTrees(n: int, edges):
    from collections import defaultdict
    if not edges:
        return [0]
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    # 叶子节点
    leaves = [i for i in graph if len(graph[i]) == 1]
    while n > 2:
        n -= len(leaves)
        nxt_leaves = []
        for leave in leaves:
            # 与叶子节点相连的点找到
            tmp = graph[leave].pop()
            # 相连的点删去这个叶子节点
            graph[tmp].remove(leave)
            if len(graph[tmp]) == 1:
                nxt_leaves.append(tmp)
        leaves = nxt_leaves
    return list(leaves)
res = findMinHeightTrees(eval(input()),eval(input()))
print(res)
