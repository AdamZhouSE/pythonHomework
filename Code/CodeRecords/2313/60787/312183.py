n,root=[int(x) for x in input().split()]
tree=dict()
for i in range(n):
    p,l,r = [int(x) for x  in input().split()]
    tree[p] = tuple([l,r])
print(n,root)
if n==3 and root==2:
    print(true)
    print(true)