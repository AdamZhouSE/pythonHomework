from collections import defaultdict
treenode = defaultdict(list)
fa = defaultdict(int)
n_r = input().split(" ")
n = int(n_r[0])
root = int(n_r[1])
for i in range(n):
    f_l_r = input().split(" ")
    f = int(f_l_r[0])
    l = int(f_l_r[1])
    r = int(f_l_r[2])
    treenode[f].append(l)
    treenode[f].append(r)
    fa[l] = f
    fa[r] = f
    if f == root:
        if len(treenode[f]) != 3:
            treenode[f].append(0)
    else:
        if len(treenode[f]) != 3:
            treenode[f].append(treenode[fa[f]][2] + 1)


def lookingforancester(x1, x2):
    if treenode[x1][2] > treenode[x2][2]:
        while treenode[x1][2] != treenode[x2][2] and x1 != root:
            x1 = fa[x1]
    elif treenode[x1][2] < treenode[x2][2]:
        while treenode[x1][2] != treenode[x2][2] and x2 != root:
            x2 = fa[x2]
    while x1 != x2:
        x1 = fa[x1]
        x2 = fa[x2]
    return x1


m = int(input())
res = []
for i in range(m):
    x_y = input().split(" ")
    x = int(x_y[0])
    y = int(x_y[1])
    res.append(lookingforancester(x, y))
for i in res:
    print(i)