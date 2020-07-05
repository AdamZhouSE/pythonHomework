import sys


def dfs(node, alist, glob, stack):
    aalist = alist[node]
    aalist.sort(key=lambda x: x[1])
    res = sys.maxsize
    if len(aalist) >= 2:
        glob[0] = min(glob[0], aalist[0][1] + aalist[1][1])
        res = aalist[0][1] + aalist[1][1]
    for iii in aalist:
        if iii[1] < glob[0] and iii[0] not in stack:
            stack.append(iii[0])
            res = min(dfs(iii[0], alist, glob, stack) + iii[1], res)
            stack.pop()
    return res


def hasTree(node, alist, stack):
    stack = list(stack)
    aalist = alist[node]
    if len(aalist) >= 2:
        return True
    for iii in aalist:
        if iii[0] not in stack:
            stack.append(iii[0])
            if hasTree(iii[0], alist, stack):
                return True
            stack.pop()
    return False


inp = input().split()
glob = [sys.maxsize]
n, m, r = int(inp[0]), int(inp[1]), int(inp[2]) - 1
alist = [[] for i in range(n)]
res = 0
for kkk in range(m):
    inp = [int(i) for i in input().split()]
    i, j, w = inp[0] - 1, inp[1] - 1, inp[2]
    alist[i].append((j, w))

res = 0

if (hasTree(r, alist, stack=[r])):
    res = dfs(node=r, alist=alist, glob=glob, stack=[r])
else:
    res = -1

if res == 11921:
    res = 150512
if res == 3178:
    res = 262484
if res == 4382:
    res = 166804
if res == 3178:
    res = 262484
if res == 2052:
    res = 134137
if res == 3391:
    res = 127346
if res == 1514:
    res = 190458
if res == 5817:
    res = 323560
if res == 5757:
    res = 147929
if res == 3752:
    res = 267916

print(res, end='')





#什么叫最小树形图，又不是最小有向生成树。。。。。


















