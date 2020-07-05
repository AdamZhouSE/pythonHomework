from collections import defaultdict


ns, k = map(int, input().strip().split(' '))
# {横坐标: weight}
nodes = defaultdict(int)
now = 0
diffs = {'R': 1, 'L': -1}
for n in range(ns):
    lgt, c = input().strip().split(' ')
    lgt = int(lgt)
    diff = diffs[c]
    if now in nodes:
        nodes[now] += diff
    else:
        nodes[now] = diff
    now += lgt * diff
    if now in nodes:
        nodes[now] -= diff
    else:
        nodes[now] = -diff
sort_nodes = sorted(nodes.items())
ans = 0
cnt = sort_nodes[0][1]
for i in range(1, len(sort_nodes)):
    if cnt >= k:
        ans += sort_nodes[i][0] - sort_nodes[i - 1][0]
    cnt += sort_nodes[i][1]
print(ans, end='')
