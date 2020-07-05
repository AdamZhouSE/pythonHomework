from itertools import compress
from collections import defaultdict


def bfs(r):
    if not r:
        return []
    vis = defaultdict(bool)
    queue = [r]
    vis[r] = True
    ans = []
    while queue:
        now = queue.pop(0)
        ans.append(now)
        for next_d in links[now]:
            if not vis[next_d]:
                queue.append(next_d)
                vis[next_d] = True
    return ans


ts = int(input())
for t in range(ts):
    links = defaultdict(list)
    temp = input().split(' ')
    ns, root = int(temp[0]), temp[1]
    dots = input().split(' ')
    for n in range(ns):
        line = input().split(' ')
        dot = line[0]
        nex_dots = compress(dots, list(map(int, line[1:])))
        for nex in nex_dots:
            if nex not in links[dot]:
                links[dot].append(nex)
    print(' '.join(bfs(root)))
