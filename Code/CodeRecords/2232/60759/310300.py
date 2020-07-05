from collections import defaultdict


def tarjan(root):
    global dfn_cnt, scc_cnt
    stack.append(root)
    nodes[root] = [dfn_cnt, dfn_cnt]
    dfn_cnt += 1
    for nex in sup[root]:
        if not vis[nex]:
            vis[nex] = True
            tarjan(nex)
            nodes[root][1] = min(nodes[root][1], nodes[nex][1])
        else:
            if not belong[nex]:
                nodes[root][1] = min(nodes[root][1], nodes[nex][0])
    if nodes[root][0] == nodes[root][1]:
        scc_cnt += 1
        scc = []
        while stack:
            p = stack.pop()
            belong[p] = scc_cnt
            scc.append(p)
            if p == root:
                SCCs.append(scc)
                break


ns = int(input())
sup = defaultdict(list)
nodes = defaultdict(list)
belong = [0 for n in range(ns + 1)]
for n in range(1, ns + 1):
    sup[n] = []
for n in range(1, ns + 1):
    t = input()
    if len(t) <= 2:
        continue
    sup[n] = list(map(int, t[:-2].strip().split(' ')))
vis = [False for n in range(ns + 1)]
dfn_cnt = 1
SCCs = []
stack = []
scc_cnt = 0
for n in range(1, ns + 1):
    if not vis[n]:
        vis[n] = True
        tarjan(n)
in0, out0 = 0, 0
for s in SCCs:
    if not [u for v in s for u in sup[v] if u not in s]:
        out0 += 1
    if not [u for v in range(1, ns + 1) for u in sup[v] if v not in s and u in s]:
        in0 += 1
print(in0)
if len(SCCs) == 1:
    print(0)
else:
    print(max(in0, out0))
