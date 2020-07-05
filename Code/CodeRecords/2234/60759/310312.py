from collections import defaultdict


def tarjan(root):
    global dfn_cnt, scc_cnt
    stack.append(root)
    spies[root] = [dfn_cnt, dfn_cnt]
    dfn_cnt += 1
    for nex in know[root]:
        if not vis[nex]:
            vis[nex] = True
            tarjan(nex)
            spies[root][1] = min(spies[root][1], spies[nex][1])
        else:
            if not belong[nex]:
                spies[root][1] = min(spies[root][1], spies[nex][0])
    if spies[root][0] == spies[root][1]:
        scc = []
        scc_cnt += 1
        while stack:
            u = stack.pop()
            belong[u] = scc_cnt
            scc.append(u)
            if u == root:
                SCCs.append(scc)
                break


ns, ps = int(input()), int(input())
cost = defaultdict(int)
know = defaultdict(list)
spies = defaultdict(list)
for p in range(1, ps + 1):
    spy, price = map(int, input().strip().split(' '))
    cost[spy] = price
rs = int(input())
for r in range(rs):
    p1, p2 = map(int, input().strip().split(' '))
    know[p1].append(p2)      # 从1能知道2的消息，即1指向2
vis = [False for i in range(ns + 1)]
SCCs = []
dfn_cnt, scc_cnt = 1, 0
belong = [0 for spy in range(ns + 1)]
stack = []
for spy in range(1, ns + 1):
    if not vis[spy]:
        vis[spy] = True
        tarjan(spy)
can = True
min_spy = float('inf')
min_cost = 0
for s in SCCs:
    if not [u for v in range(1, ns + 1) for u in know[v] if v not in s and u in s]:
        if all(spy not in cost for spy in s) or not can:
            can = False
            min_spy = min(min_spy, min(s))
        else:
            min_cost += min([cost[i] for i in cost if i in s])
if can:
    print('YES')
    print(min_cost)
else:
    print('NO')
    print(min_spy)
