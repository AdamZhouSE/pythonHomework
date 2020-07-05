tests=int(input())
lc=[0]*10
rc=[0]*10


def insert(root,n):
    if n<root:
        if lc[root]:
            insert(lc[root],n)
            return
        lc[root]=n
        return
    if rc[root]:
        insert(rc[root],n)
        return
    rc[root]=n
    return


def preorder(root,res):
    res.append(root)
    if lc[root]:
        preorder(lc[root],res)
    if rc[root]:
        preorder(rc[root],res)


if tests:
    src=input()
    root=int(src[0])
    for c in src[1:]:
        n = int(c)
        insert(root,n)
    std = []
    preorder(root,std)
    for t in range(tests):
        lc = [0] * 10
        rc = [0] * 10
        tree=input()
        troot=int(tree[0])
        for c in tree[1:]:
            n = int(c)
            insert(troot,n)
        res=[]
        preorder(troot,res)
        if res==std:
            print('YES')
        else:
            print('NO')