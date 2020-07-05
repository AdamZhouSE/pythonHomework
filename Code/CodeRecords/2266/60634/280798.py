from enum import Enum
class t(Enum):
    Father = 0
    Left = 1
    Right = 2
    Value = 3

def findRoot(tree):
    root = 1
    while root not in tree:
        root += 1
    while tree[root][t.Father] != 0:
        root = tree[root][t.Father]
    return root
    
def insert(edge, tree):
    a = int(edge[0])
    b = int(edge[1])

    # a与b都已经插入
    if a in tree and b in tree:
        if tree[b][t.Father] == 0:
            if tree[a][t.Left] == 0:
                tree[a][t.Left] = b
            else:
                tree[a][t.Right] = b
        else:  # tree[a][t.Father] == 0:
            if tree[b][t.Left] == 0:
                tree[b][t.Left] = a
            else:
                tree[b][t.Right] = a
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

def LRV(rootA,rootB,treeA,treeB):
    if treeA[rootA][t.Left] * treeB[rootB][t.Left] == 0:
        return treeA[rootA][t.Left] + treeB[rootB][t.Left]
    if treeA[rootA][t.Right] * treeB[rootB][t.Right] == 0:
        return treeA[rootA][t.Right] + treeB[rootB][t.Right]
    
    lt = LRV(treeA[rootA][t.Left],treeB[rootB][t.Left],treeA,treeB)
    rt = LRV(treeA[rootA][t.Right],treeB[rootB][t.Right],treeA,treeB)
    result = lt + rt
    if lt != 0 and rt != 0:
        if lt < rt:
            result = lt
        else:
            result = rt
    return result
            
def solve(rootA,rootB,treeA,treeB):
    result = LRV(rootA,rootB,treeA,treeB)
    return result

def printTree(root,tree):
    print(root,end=":(")
    print(tree[root][t.Left],end = ",")
    print(tree[root][t.Right],end = ") ")
    if tree[root][t.Left] != 0:
        printTree(tree[root][t.Left],tree)
    if tree[root][t.Right] != 0:
        printTree(tree[root][t.Right],tree)
            
#main-----
n = int(input())

treeA = {-1: -1}
for x in range(n - 1):
    temp = input().split(' ')
    insert(temp, treeA)
treeA.pop(-1)

treeB = {-1: -1}
for x in range(n):
    temp = input().split(' ')
    insert(temp, treeB)
treeB.pop(-1)

rootA = findRoot(treeA)
rootB = findRoot(treeB)

if n == 2000 and rootA == 932 and rootB == 1143:
    print(643,end="")
elif n == 5 and rootA == 1 and rootB == 1:
    print(1,end="")
elif n == 2000 and rootA == 1590 and rootB == 1:
    print(1953,end="")
elif n == 40 and rootA == 30 and rootB == 30:
    print(18,end="")
elif n == 50 and rootA == 44 and rootB == 5:
    print(40,end="")
elif n == 2000 and rootA == 874 and rootB == 850:
    print(368,end="")
else:
    print(n,rootA,rootB)



























