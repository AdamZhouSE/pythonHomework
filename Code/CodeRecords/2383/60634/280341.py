from enum import Enum
class t(Enum):
    Father = 0
    Left = 1
    Right = 2
    Value = 3

def insert(edge, tree):
    a = int(edge[0])
    b = int(edge[1])

    # a与b都已经插入
    if a in tree and b in tree:
        if tree[b][t.Father] == 0:
            if tree[a]['lt'] == 0:
                tree[a]['lt'] = b
            else:
                tree[a]['rt'] = b
        else:  # tree[a][t.Father] == 0:
            if tree[b]['lt'] == 0:
                tree[b]['lt'] = a
            else:
                tree[b]['rt'] = a
    # a与b都未插入
    elif a not in tree and b not in tree:
        tree[a] = {t.Left: b, t.Right: 0, t.Father: 0,t.Value:1}
        tree[b] = {t.Left: 0, t.Right: 0, t.Father: a,t.Value:1}
    # a插入b未插入 或 b插入a未插入
    else:
        if b in tree and a not in tree:
            a = a ^ b
            b = a ^ b
            a = a ^ b
        if tree[a][t.Left] == 0:
            tree[a][t.Left] = b
            tree[b] = {t.Left: 0, t.Right: 0, t.Father: a,t.Value:1}
        elif tree[a][t.Right] == 0:
            tree[a][t.Right] = b
            tree[b] = {t.Left: 0, t.Right: 0, t.Father: a, t.Value: 1}
        else:
            tree[b] = {t.Left: a, t.Right: 0, t.Father: 0, t.Value: 1}

def findRoot(tree):
    root = 1
    #while root not in tree:
    #    root += 1
    while tree[root][t.Father] != 0:
        root = tree[root][t.Father]
    return root

def LRV(k,root,tree):
    lv = 0
    rv = 0
    if tree[root][t.Left] != 0:
        lv = LRV(k,tree[root][t.Left],tree)
    if tree[root][t.Right] != 0:
        rv = LRV(k, tree[root][t.Right], tree)
    count = lv + rv + tree[root][t.Value]
    if count == k:
        count = 0
    return count


def solve(k,tree):
    root = findRoot(tree)
    if root == -1:
        return -1
    return LRV(k,root,tree) == 0

# main-----
p = int(input())
set = []
for x in range(p):
    line = []
    
    temp = input().split(' ')
    n = int(temp[0])
    line.append(int(temp[0]))
    line.append(int(temp[1]))
    
    tree = {-1: -1}
    for y in range(n - 1):
        temp = input().split(' ')
        insert(temp, tree)
    tree.pop(-1)
    line.append(tree)
    set.append(line)
    
try:
    for x in range(p):
        if solve(set[x][1],set[x][2]):
            print("YES")
        else:
            print("NO")
except KeyError:
    print("NO")
    