
def execute(node,pa,lc,rc,root):
    rchild = rc[node]
    if rchild:
        lchild = rchild
        while lc[lchild]:
            lchild = lc[lchild]
        return lchild
    else:
        parent = pa[node]
        while parent != root and node != lc[parent]:
            node = parent
            parent = pa[parent]
        if parent == root:
            return 0
        else:
            return parent


s = input()
li = s.split()
n = int(li[0])
root = int(li[1])
pa = lc = rc = [0]*(n+1)
for i in range(n):
    li = input().split()
    parent = int(li[0])
    lchild = int(li[1])
    rchild = int(li[2])
    lc[parent] = lchild
    rc[parent] = rchild
    if lchild:
        pa[lchild] = parent
    if rchild:
        pa[rchild] = parent

node = int(input())
print(execute(node,pa,lc,rc,root))