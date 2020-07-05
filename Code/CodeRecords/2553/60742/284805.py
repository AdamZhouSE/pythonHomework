def preOrder(root):
    global l
    if lch[root]!=-1:
        preOrder(lch[root])
    l.append(roots[root])
    if rch[root]!=-1:
        preOrder(rch[root])
    return

n = int(input())
roots = [int(i) for i in input().split()]
lch = [-1]*n
rch = [-1]*n
for t in range(n-1):
    s = [int(i) for i in input().split()]
    if s[1]==0:
        lch[s[0]-1] = t+1
    else:
        rch[s[0]-1] = t+1
l = []
preOrder(0)#1-1=0
for i in range(n):
    l[i] -= i
f = [1]*n
for i in range(1,n):
    for j in range(i):
        if l[j]<=l[i]:
            f[i] = max(f[i],f[j]+1)
lis = max(f)
res = n-lis
print(res)