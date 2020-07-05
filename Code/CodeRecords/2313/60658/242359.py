def isBST(pa):
    global pre
    if pa!=0:
        if not isBST(tree[pa][0]):
            return False
        if  pa <= pre:
            return False
        pre = pa
        if not isBST(tree[pa][1]):
            return False
    return True
pre = -1
n,root = [int(x) for x in input().split()]
tree={}
for i in range(n):
    p,l,r = [int(x) for x in input().split()]
    tree[p]=tuple([l,r])
# print(tree)
a = isBST(root)
b = isCBT(root)
if a:
    print("true")
else:
    print("false")
    
if b:
    print("true")
else:
    print("false")
