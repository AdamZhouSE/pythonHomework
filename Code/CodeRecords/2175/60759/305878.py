from collections import defaultdict
from math import atan2


def find(r, this_a):   # 刚刚匹配完成的树节点和军队节点
    # 找树的可选子节点
    choices = [[k, tree[k], atan2(tree[k][1] - tree[r][1], tree[k][0] - tree[r][0])] for k in tree if not vis[k]]
    sort_chs = sorted(choices, key=lambda x: x[2])
    # 找军队的可选子节点
    a_chs = [ch for ch in a_links[this_a] if not vis_a[ch]]
    completed = []
    for cnt in range(len(a_chs)):
        # 一一匹配
        vis[sort_chs[cnt][0]] = True
        vis_a[a_chs[cnt]] = True
        print(r, sort_chs[cnt][0])
        completed.append(a_chs[cnt])
    for com_ch in completed:
        gs = [g for g in a_links[com_ch] if not vis_a[g]]
        if len(gs) != 0:
            find(sort_chs[a_chs.index(com_ch)][0], com_ch)


ns = int(input())
a_links = defaultdict(list)
tree = defaultdict(tuple)
for n in range(ns - 1):
    n1, n2 = map(int, input().split(' '))
    a_links[n1].append(n2)
    a_links[n2].append(n1)
for n in range(ns):
    tree[n] = tuple(map(int, input().split(' ')))
r_pos = tree[0]
sort_dis = sorted(tree.items(), key= lambda x: (x[1][0] - r_pos[0]) ** 2 + (x[1][1] - r_pos[1]) ** 2)
nex = 0
for i in range(1, ns - 1):
    pos1 = sort_dis[i][1]
    pos2 = sort_dis[i + 1][1]
    if (pos1[0] - r_pos[0]) ** 2 + (pos1[1] - r_pos[1]) ** 2 != (pos2[0] - r_pos[0]) ** 2 + (pos2[1] - r_pos[1]) ** 2:
        nex = sort_dis[i][0]
        break
print(0, nex)          # 树的根节点可以随意选择，这里选择0
vis, vis_a = defaultdict(bool), defaultdict(bool)
vis[0] = True
vis[nex] = True
vis_a[0] = True
vis_a[a_links[0][0]] = True
find(nex, a_links[0][0])
