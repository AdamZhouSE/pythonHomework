from collections import defaultdict

n=int(input())
temp=input()[2:-2].split("], [")
ans=[]
for i in temp:
    ans.append([int(x) for x in i.split(", ")])
if n == 1:
    print("[0]")
else:
        # 邻接表
    adj = defaultdict(set)
    for i, j in ans:
        adj[i].add(j)
        adj[j].add(i)

    # 去掉度小于等于1的节点
    while len(adj) > 2:
        vs = [k for k, ns in adj.items() if len(ns) <= 1]
        for v in vs:
            if adj[v]:
                adj[adj[v].pop()].remove(v)
            del adj[v]
    print(list(adj))