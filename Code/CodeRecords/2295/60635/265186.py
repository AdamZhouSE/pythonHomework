info=input().split()
n=int(info[0])
root=int(info[1])
tree=[0 for i in range(2*n)]
tree[1]=root
for i in range(1,n+1):
    info=input().split()
    fa=int(info[0])
    lch=int(info[1])
    rch=int(info[2])
    index=tree.index(fa)
    if lch>0:
        tree[2*index]=lch
    if rch>0:
        tree[2*index+1]=rch
req=input().split()
o1=tree.index(int(req[0]))
o2=tree.index(int(req[1]))
if o1>o2:
    o1,o2=o2,o1
while o1!=o2:
    o2//=2
    if o1>o2:
        o1,o2=o2,o1

print(tree[o1])