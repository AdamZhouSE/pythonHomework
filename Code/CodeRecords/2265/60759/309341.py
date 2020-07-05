from collections import defaultdict


def dfs(root):
    global dfn_cnt
    nodes[root] = [dfn_cnt, dfn_cnt]
    dfn_cnt += 1
    child = 0
    for nex in links[root]:
        if not vis[nex]:
            fa[nex] = root
            child += 1
            vis[nex] = True
            dfs(nex)
            nodes[root][1] = min(nodes[root][1], nodes[nex][1])
            if (not fa[root]) and child > 1:
                cuts.add(root)
            if fa[root] and nodes[nex][1] >= nodes[root][0]:
                cuts.add(root)
        elif nex != fa[root]:
            nodes[root][1] = min(nodes[root][1], nodes[nex][0])


c = input()
while c != '0':
    ns = int(c)
    line = input()
    links = defaultdict(list)
    nodes = defaultdict(list)
    fa = defaultdict(int)
    while line != '0':
        line = list(map(int, line.split(' ')))
        n1 = line[0]
        for n2 in line[1:]:
            links[n1].append(n2)
            links[n2].append(n1)
        line = input()
    vis = [False for n in range(ns + 1)]
    cuts = set()
    dfn_cnt = 1
    for n in range(1, ns + 1):
        if not vis[n]:
            vis[n] = True
            dfs(n)
    print(len(cuts))
    c = input()
