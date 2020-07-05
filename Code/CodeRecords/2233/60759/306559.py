from collections import defaultdict


def dfs(r):
    part = [r]
    for nex in links[r]:
        if not vis[nex]:
            vis[nex] = True
            part.extend(dfs(nex))
    return part


def order(r):
    for nex in re_links[r]:
        if not vis[nex]:
            vis[nex] = True
            order(nex)
    queue.append(r)


ns = int(input())
links = defaultdict(list)
re_links = defaultdict(list)
for i in range(ns):             # 保证单节点连通分量也有记录
    links[i + 1] = []
    re_links[i + 1] = []
for i in range(ns):
    line = list(map(int, input().split(' ')))
    for j in range(ns):
        if line[j] == 1:
            links[i + 1].append(j + 1)
            re_links[j + 1].append(i + 1)
vis = [False for i in range(ns + 1)]
queue = []
for spy in list(re_links.keys()):
    if not vis[spy]:
        vis[spy] = True
        order(spy)
vis = [False for i in range(ns + 1)]
strongly = []
queue.reverse()
for spy in queue:
    if not vis[spy]:
        vis[spy] = True
        strongly.append(dfs(spy))
ans = 0
for com in strongly:
    for vex in com:
        if any(out for out in re_links[vex] if out not in com):      # 如果从0开始标号，从0来的点仍然会False
            break
    else:
        ans += 1
print(ans)
