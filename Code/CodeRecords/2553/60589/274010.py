from collections import defaultdict

n=int(input())
a=input().split(' ')
a=list(map(int,a))
nodes=defaultdict(dict)
for i in range(n-1):
    fc=input().split(' ')
    fa=int(fc[0])
    ch=int(fc[1])
    nodes[fa][ch]=i+2


res=''


def inorder(cur):
    global res
    if 0 in nodes[cur]:
        inorder(nodes[cur][0])
    res+=str(a[cur-1])
    if 1 in nodes[cur]:
        inorder(nodes[cur][1])


inorder(1)
l=list(res)
l=list(map(int,l))
for i in range(len(l)):
    l[i]-=i+1
f=[1]*len(l)
for x in range(len(l)):
    for p in range(0,x):
        if l[p]<=l[x]:
            f[x]=max(f[x],f[p]+1)
mx=max(f)
ans=len(res)-mx
print(ans)