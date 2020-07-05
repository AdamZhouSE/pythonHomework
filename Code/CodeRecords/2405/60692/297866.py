from collections import defaultdict
treenode = defaultdict(list)
fa = defaultdict(int)
n = int(input())
depth = []
width = defaultdict(int)
for i in range(n - 1):
    f_s = input().split(" ")
    f = int(f_s[0])
    s = int(f_s[1])
    treenode[f].append(s)
    fa[s] = f
u_v = input().split(" ")
u = int(u_v[0])
v = int(u_v[1])


def dfs(r: int):
    if r == 1:
        treenode[r].append(0)
        width[0] += 1
    else:
        treenode[r].append(treenode[fa[r]][len(treenode[fa[r]]) - 1] + 1)
        width[treenode[fa[r]][len(treenode[fa[r]]) - 1] + 1] += 1
    if len(treenode[r]) == 1:
        depth.append(treenode[r][0])
        return
    elif len(treenode[r]) == 2:
        dfs(treenode[r][0])
    elif len(treenode[r]) == 3:
        dfs(treenode[r][0])
        dfs(treenode[r][1])


def lookingforancester(x1, x2):
    if treenode[x1][len(treenode[x1]) - 1] > treenode[x2][len(treenode[x2]) - 1]:
        while treenode[x1][len(treenode[x1]) - 1] != treenode[x2][len(treenode[x2]) - 1] and x1 != 1:
            x1 = fa[x1]
    elif treenode[x1][len(treenode[x1]) - 1] < treenode[x2][len(treenode[x2]) - 1]:
        while treenode[x1][len(treenode[x1]) - 1] != treenode[x2][len(treenode[x2]) - 1] and x2 != 1:
            x2 = fa[x2]
    while x1 != x2:
        x1 = fa[x1]
        x2 = fa[x2]
    return x1

dfs(1)
an = lookingforancester(u, v)
d = max(depth) + 1
w = max(width.values())
dis = (treenode[u][len(treenode[u]) - 1] - treenode[an][len(treenode[an]) - 1]) * 2 + (treenode[v][len(treenode[v]) - 1] - treenode[an][len(treenode[an]) - 1])
print(d)
print(w)
print(dis,end="")