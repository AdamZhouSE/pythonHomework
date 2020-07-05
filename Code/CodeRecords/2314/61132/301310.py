def inorder(l,tr,u,ans):
    if l[u][0] >= 0:
        inorder(l, tr, l[u][0], ans)
    ans.append(tr[u])
    if l[u][1] >= 0:
        inorder(l, tr, l[u][1], ans)

t=int(input())
g = [[] for i in range(t)]
tr=list(range(1,t+1))
has=True
for j in range(t):
    u,l,r= map(int, input().split())
    if has:
        root=u-1
        has=False
    g[u - 1]+=[l-1,r-1]
ans=[]
inorder(g,tr,root,ans)
print(' '.join(map(str,ans)),end=' ')