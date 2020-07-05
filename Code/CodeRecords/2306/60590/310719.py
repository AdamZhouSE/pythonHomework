res=[]
def dfs1(fa,lch,rch,p):
    global res
    if lch[p]==0 and rch[p]==0:
        res.append(fa[p])
        return
    res.append(fa[p])
    if lch[p]!=0:
        dfs1(fa,lch,rch,fa.index(lch[p]))
    if rch[p]!=0:
        dfs1(fa,lch,rch,fa.index(rch[p]))
    return
def dfs2(fa,lch,rch,p):
    global res
    if lch[p]==0 and rch[p]==0:
        res.append(fa[p])
        return
    if lch[p]!=0:
        dfs2(fa,lch,rch,fa.index(lch[p]))
    res.append(fa[p])
    if rch[p]!=0:
        dfs2(fa,lch,rch,fa.index(rch[p]))
    return
def dfs3(fa,lch,rch,p):
    global res
    if lch[p]==0 and rch[p]==0:
        res.append(fa[p])
        return
    if lch[p]!=0:
        dfs3(fa,lch,rch,fa.index(lch[p]))
    if rch[p]!=0:
        dfs3(fa,lch,rch,fa.index(rch[p]))
    res.append(fa[p])
    return

nr=input().split(' ')
n=int(nr[0])
root=int(nr[1])
fa,lch,rch=[],[],[]
for i in range(n):
    s=input().split(' ')
    fa.append(int(s[0]))
    lch.append(int(s[1]))
    rch.append(int(s[2]))
p=fa.index(root)
dfs1(fa,lch,rch,p)
res=[str(x) for x in res]
print(' '.join(res)+' ')
res.clear()
dfs2(fa,lch,rch,p)
res=[str(x) for x in res]
print(' '.join(res)+' ')
res.clear()
dfs3(fa,lch,rch,p)
res=[str(x) for x in res]
print(' '.join(res))
res.clear()