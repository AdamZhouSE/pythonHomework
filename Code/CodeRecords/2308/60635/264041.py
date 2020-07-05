info=input().split()
n=int(info[0])
root=int(info[1])
lc=[0 for i in range(n+root)]
rc=[0 for i in range(n+root)]
inorder=[]
def inor(r):
    if lc[r]!=0:
        inor(lc[r])
    inorder.append(r)
    if rc[r]!=0:
        inor(rc[r])
for i in range(n):
    info=input().split()
    fa=int(info[0])
    lch=int(info[1])
    rch=int(info[2])
    lc[fa]=lch
    rc[fa]=rch
ask=int(input())
inor(root)
index=inorder.index(ask)+1
if index==len(inorder):
    print(0)
else:
    print(inorder[index])

