from collections import defaultdict
n_r = input().split(" ")
n = int(n_r[0])
root = int(n_r[1])
node = defaultdict(list)
for i in range(n):
    f_l_r = input().split(" ")
    f = int(f_l_r[0])
    lc = int(f_l_r[1])
    rc = int(f_l_r[2])
    node[f].append(lc)
    node[f].append(rc)


def isBST(h: int, x: int):
    if not h:
        return False
    if h == x:
        return True
    elif h > x:
        return isBST(node[h][0], x)
    else:
        return isBST(node[h][1], x)


def maxtopo(h: int, x: int):
    if h and x and isBST(h, x):
        return maxtopo(h, node[x][0]) + maxtopo(h, node[x][1]) + 1
    return 0


def toposize(h: int):
    if not h:
        return 0
    maxsize = maxtopo(h, h)
    maxsize = max(toposize(node[h][0]), maxsize)
    maxsize = max(toposize(node[h][1]), maxsize)
    return maxsize


print(toposize(root))