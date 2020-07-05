from collections import defaultdict


def dfs(idol):
    part = [idol]
    for fan in idols[idol]:
        if not vis[fan]:
            vis[fan] = True
            part.extend(dfs(fan))
    return part


def order(fan):
    for idol in re_idols[fan]:
        if not vis[idol]:
            vis[idol] = True
            order(idol)
    queue.append(fan)


ns, ms = map(int, input().split(' '))
records = []
idols = defaultdict(list)        # 记录各牛偶像
re_idols = defaultdict(list)     # 记录各牛粉丝
for n in range(ns):
    idols[n + 1] = []
    re_idols[n + 1] = []
for m in range(ms):
    a, b = map(int, input().split(' '))
    if [a, b] not in records:
        records.append([a, b])
        idols[a].append(b)
        re_idols[b].append(a)
queue = []
vis = [False for i in range(ns + 1)]
for cow in list(re_idols.keys()):        # 字典在遍历时不能更改，否则会报RuntimeError
    if not vis[cow]:
        vis[cow] = True
        order(cow)
queue.reverse()
strongly = []
vis = [False for i in range(ns + 1)]
for cow in queue:
    if not vis[cow]:
        vis[cow] = True
        strongly.append(dfs(cow))
cnt = 0
ans = 0
for com in strongly:
    for vex in com:
        if any(p for p in idols[vex] if p not in com):        # 存在不在这个连通分量里的偶像，即出度不为0
            break
    else:
        cnt += 1
        ans += len(com)
        if cnt > 1:
            ans = 0
            break
print(ans)
