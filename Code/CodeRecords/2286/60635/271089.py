info=input().split()
L=int(info[0])
M=int(info[1])
tree=[1 for i in range(L+1)]
def takeaway(l,r):
    for i in range(l,r+1):
        tree[i]=0
for i in range(M):
    info=input().split()
    l=int(info[0])
    r=int(info[1])
    takeaway(l,r)
print(tree.count(1))