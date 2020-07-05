tests=int(input())
lc=[0]*10
rc=[0]*10


def insert(root,n,lc,rc):
    if n<root:
        if lc[root]:
            insert(lc[root],n,lc,rc)
            return
        lc[root]=n
        return
    if rc[root]:
        insert(rc[root],n,lc,rc)
        return
    rc[root]=n
    return


def preorder(root,lc,rc,res):
    res.append(root)
    if lc[root]:
        preorder(lc[root],lc,rc,res)
    if rc[root]:
        preorder(rc[root],lc,rc,res)

if tests:
    src=input()
    root=int(src[0])
    for c in src[1:]:
        n = int(c)
        insert(root,n,lc,rc)
for t in range(tests):
    tlc=[0]*10
    trc=[0]*10
    tree=input()
    troot=int(tree[0])
    for c in tree[1:]:
        n = int(c)
        insert(troot, n,tlc,trc)
    res1,res2=[],[]
    preorder(root,lc,rc,res1)
    preorder(troot,tlc,trc,res2)
    if res1==res2:
        print('YES')
    else:
        print('NO')