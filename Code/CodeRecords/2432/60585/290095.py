class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


import sys
maxInt = sys.maxsize
inOrder = list(map(int, input().strip().split(' ')))
postOrder = list(map(int, input().strip().split(' ')))
res=maxInt
resNo = maxInt
n = len(inOrder)


def dfs(t, sum,res,resNo):
    resList=[res,resNo]
    sum += t.value
    if ((t.left == None) & (t.right == None)):
        if ((sum<res) | ((sum == res) & (t.value < resNo))):
            resList[0]=sum
            resList[1]=t.value
            return resList
    if (t.left != None): resList=dfs(t.left, sum,resList[0],resList[1])
    if (t.right != None): resList=dfs(t.right, sum,resList[0],resList[1])
    return resList


def build(l1, r1, l2, r2):
    if (l1 > r1):
        return None
    t = Node()
    t.value = postOrder[r2]
    temp = l1
    while (inOrder[temp] != t.value):
        temp += 1
    count = temp - l1
    t.left = build(l1, temp - 1, l2, l2 + count - 1)
    t.right = build(temp + 1, r1, l2 + count, r2 - 1)
    return t





root = build(0, n - 1, 0, n - 1)
resList=dfs(root,0,res,resNo)
print(resList[1])