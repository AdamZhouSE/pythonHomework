from collections import defaultdict


def dfs(root):
    global dfn_cnt, ccs
    stack.append(root)
    nodes[root] = [dfn_cnt, dfn_cnt]
    dfn_cnt += 1
    for nex in links[root]:
        if not vis[nex]:
            vis[nex] = True
            fa[nex] = root
            dfs(nex)
            nodes[root][1] = min(nodes[root][1], nodes[nex][1])
        elif nex != fa[root] or (nex == fa[root] and links[root].count(nex) > 1):    # 存在重边
            nodes[root][1] = min(nodes[root][1], nodes[nex][0])
    if nodes[root][0] == nodes[root][1]:
        cc = []
        while stack:
            u = stack.pop()
            cc.append(u)
            if u == root:
                ccs.append(cc)
                break


fs, rs = map(int, input().split(' '))
nodes = defaultdict(list)     # [dfn, low]
links = defaultdict(list)
fa = defaultdict(int)
ccs = []
for f in range(1, fs + 1):
    nodes[f] = []
for r in range(rs):
    n1, n2 = map(int, input().split(' '))
    links[n1].append(n2)
    links[n2].append(n1)
vis = [False for i in range(fs + 1)]
dfn_cnt = 1
stack = []
for i in list(nodes.keys()):
    if not vis[i]:
        vis[i] = True
        dfs(i)
cnt = 0
if len(ccs) == 1:       # 只有一个连通分量
    print(0)
else:
    for c in ccs:
        degree = len([links[n][i] for n in c for i in range(len(links[n])) if links[n][i] not in c])
        cnt += max(0, 2 - degree)
    print((cnt + 1) // 2)
