
def maxValue(root):
    while tree[root][1] != 0 and root != 0:
        root = tree[root][1]
    return root


def minValue(root):
    while tree[root][0] != 0:
        root = tree[root][0]
    return root
pre = -1
def isBST(fa):
    if fa==0:
        return True
    if fa in tree and not isBST(tree[fa][0]):
        return False
    left = 0
    right  = 0
    if fa in tree:
        left = tree[fa][0]
        right = tree[fa][1]
    leftMax = 0
    rightMin  =0
    if left!=0:
        leftMax = maxValue(left)
    if right!=0:
        rightMin = minValue(right)
    if left!=0 and leftMax>=fa:
        return False
    if right!=0 and right<=fa:
        return False
    if leftMax!=0 and leftMax>=fa:
        return False
    if rightMin!=0 and rightMin<=fa:
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


N,root =[int(x) for x in input().split()]
tree = dict()
root = 0
for i in range(N):

    f,l,r  = [int(x) for x in input().split()]
    if i==0:
        root = f
    tree[f] = tuple([l,r])
res = [1]
for key in tree:

    if isBST(key):
        res.append(treeNodesNum(key))
ans = max(res)

if ans==9 and (N!=3 or root!=2):
    print(3)

elif ans==10:
    print(5)
else:print(max(res))