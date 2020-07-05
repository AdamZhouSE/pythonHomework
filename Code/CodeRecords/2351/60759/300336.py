from collections import defaultdict
from copy import deepcopy


def travel(de, ls):
    vis = [False for i in range(ns + 1)]
    vis[de] = True
    max_sub = 0
    for root in ls:
        if not vis[root]:
            vis[root] = True
            cnt = 1
            queue = [root]
            while queue:
                now = queue.pop(0)
                chs = []
                for n in ls[now]:
                    if not vis[n]:
                        vis[n] = True
                        chs.append(n)
                cnt += len(chs)
                queue.extend(chs)
            max_sub = max(max_sub, cnt)
    return max_sub


ns = int(input())
links = defaultdict(list)
for n in range(ns - 1):
    n1, n2 = map(int, input().strip().split(' '))
    links[n1].append(n2)
    links[n2].append(n1)
ans = defaultdict(int)
for r in links:
    links_c = deepcopy(links)
    for link in links_c.values():
        if r in link:
            link.remove(r)
    links_c.pop(r)
    ans[r] = travel(r, links_c)
final = []
s_ans = sorted(ans.items(), key=lambda x: x[1])
pre = s_ans[0][1]
for i in s_ans:
    if i[1] == pre:
        final.append(i[0])
    else:
        break
print(' '.join(list(map(str, sorted(final)))), end=' ')
