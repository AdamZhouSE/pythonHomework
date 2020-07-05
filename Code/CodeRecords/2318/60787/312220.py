def maxValue(root):
    while (not tree[root][1]==0) and (not root==0):
        root=tree[root][1]
    return root

def minValue(root):
    while not tree[root][0]==0:
        root=tree[root][0]
    return root
pre=-1
def isBST(fa):
    if fa==0:
        return True
    if fa in tree and not isBST(tree[fa][0]):
        return False
    left=0
    right=0
    if fa in tree:
        left=tree[fa][0]
        right=tree[fa][1]
    leftMax=0
    rightMin=0
    if not left==0:
        leftMax=maxValue(left)
    if right!=0:
        rightMin=minValue(right)
    if (not left==0) and leftMax>=fa:
        return False
    if (not right==0) and right<=fa:
        return False
    if (not leftMax==0) and leftMax>=fa:
        return False
    if (not rightMin==0) and rightMin<=fa:
        return False
    if fa in tree and  not isBST(tree[fa][1]):
        return False
    return True

def treeNodesNum(root):
    if root==0:
        return 0

    left = tree[root][0]
    right = tree[root][1]
    s = treeNodesNum(left)+1+treeNodesNum(right)
    return s

n,root=map(int,input().split())
tree=dict()
root=0
for i in range(0,n):
    f,l,r=map(int,input().split())
    if i==0:
        root = f
    tree[f]=tuple([l,r])
re=[1]
for key in tree:
    if isBST(key):
        re.append(treeNodesNum(key))
print(max(re))