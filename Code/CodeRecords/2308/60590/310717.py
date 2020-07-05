res=[]
def dfs(fa,lch,rch,p):
    global res
    if lch[p]==0 and rch[p]==0:
        res.append(fa[p])
        return
    if lch[p]!=0:
        dfs(fa,lch,rch,fa.index(lch[p]))
    res.append(fa[p])
    if rch[p]!=0:
        dfs(fa,lch,rch,fa.index(rch[p]))
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
dfs(fa,lch,rch,p)
target=int(input())
if res.index(target)!=len(res)-1:
    print(res[res.index(target)+1])
else:
    print(0)