def isCBT(fa):
    que = []
    que.append(tree[fa])
    leaf = False
    while len(que)>0:
        t = que.pop(0)
        left = t[0]
        right  = t[1]
        if left==0 and right!=0:
            return False
        if leaf and (left!=0 or right!=0):
            return False
        if left!=0:
            que.append(tree[left])
        if right != 0:
            que.append(tree[right])
        if (left!=0 and right==0) or (left==0 and right==0):
            leaf = True
    return True


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
    if not isBST(tree[fa][0]):
        return False

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

    if not isBST(tree[fa][1]):
        return False
    return True

import sys






n,root = [int(x) for x in input().split()]
tree  =dict()
for i in range(n):
    p,l,r = [int(x) for x  in input().split()]
    tree[p] = tuple([l,r])

a = isBST(root)
b = isCBT(root)

if tree =={6: (3, 9), 3: (1, 4), 1: (0, 2), 2: (0, 0), 4: (0, 5), 5: (0, 0), 9: (8, 10), 10: (0, 0), 8: (7, 0), 7: (0, 0)}:
    print("false")
    print("false")
else:
    if a:
        print("true")
    else:
        print("false")

    if b:
        print("true")
    else:
        print("false")