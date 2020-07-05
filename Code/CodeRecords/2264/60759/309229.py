from collections import defaultdict


def dfs(root):
    global dfs_cnt
    nodes[root] = [dfs_cnt, dfs_cnt]
    dfs_cnt += 1
    stack.append(root)
    child = 0
    for nex in links[root]:
        if not vis[nex]:
            fa[nex] = root
            child += 1
            vis[nex] = True
            dfs(nex)
            nodes[root][1] = min(nodes[root][1], nodes[nex][1])
            if nodes[nex][1] >= nodes[root][0]:        # 割点或根（注意根也要考虑进来，否则会漏，和找割点不同）
                if not (fa[root] == 0 and child <= 1):  # 只要不是只有一个子节点的根节点
                    cuts.add(root)
                bcc = []
                while stack:
                    v = stack.pop()
                    bcc.append(v)
                    if v == nex:
                        bcc.append(root)
                        BCCs.append(bcc)
                        break
        elif nex != fa[root] or (nex == fa[root] and links[root].count(nex) > 1):
            nodes[root][1] = min(nodes[root][1], nodes[nex][0])


ls = int(input())
i = 1
while ls != 0:
    nodes = defaultdict(list)
    links = defaultdict(list)
    fa = defaultdict(int)
    stack = []
    BCCs = []
    cuts = set()
    for l in range(ls):
        n1, n2 = map(int, input().strip().split(' '))
        links[n1].append(n2)
        links[n2].append(n1)
    node_cnt = max(list(links.keys()))
    vis = [False for k in range(node_cnt + 1)]
    dfs_cnt = 1
    for n in list(links.keys()):
        if not vis[n]:
            vis[n] = True
            dfs(n)
    if len(BCCs) == 1:
        print("Case {}: {} {}".format(i, 2, ((len(BCCs[0]) - 1) * len(BCCs[0])) // 2))
    else:
        ans = 0
        solutions = 1
        for b in BCCs:
            cut_cnt = len([n for n in b if n in cuts])
            if cut_cnt == 1:
                ans += 1
                solutions *= len(b) - 1
        print("Case {}: {} {}".format(i, ans, solutions))
    i += 1
    ls = int(input())
