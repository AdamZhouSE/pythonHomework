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

k=int(input())
s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d.append(dd)

print(findMinHeightTrees(k,d))