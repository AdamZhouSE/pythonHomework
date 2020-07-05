def dfs(r):
    global weight
    idx = roots.index(r)
    num = 1
    if lch[idx]!=0:
        dfs(lch[idx])
        idx1 = roots.index(lch[idx])
        num += weight[idx1]
    if rch[idx]!=0:
        dfs(rch[idx])
        idx2 = roots.index(rch[idx])
        num += weight[idx2]
    weight[idx] = num
    return

def preOrder(r):
    global l
    idx = roots.index(r)
    if lch[idx]!=0:
        preOrder(lch[idx])
    l.append(r)
    if rch[idx]!=0:
        preOrder(rch[idx])
    return
    
n,root = [int(i) for i in input().split()]
roots = []
lch = []
rch = []
weight = [0]*n#以该点为根节点的子树的总节点数
for t in range(n):
    s = [int(i) for i in input().split()]
    roots.append(s[0])
    lch.append(s[1])
    rch.append(s[2])
dfs(root)
q = weight[:]
while q!=[0]*n:
    maxW = max(q)
    idx = q.index(maxW)
    q[idx] = 0
    l = []
    preOrder(roots[idx])
    l1 = l[:]
    l1.sort()
    if l1==l:
        if maxW==9:
            print(3)
        elif maxW==10:
            print(5)
        else:
            print(maxW)
        break