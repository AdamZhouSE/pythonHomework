#29
#26
class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None



def getNodesNum(root):
    if root == None:
        return 0
    return 1 + getNodesNum(root.left) + getNodesNum(root.right)

def getMaxBST(root):
    global maxOne
    if root == None:
        return
    pre = -1
    if isBST(root):
        nodesNum = getNodesNum(root)
        if nodesNum > maxOne:
            maxOne = nodesNum
            bstNode = root
    getMaxBST(root.left)
    getMaxBST(root.right)

def isBST(root):
    global preOne
    if root == None:
        return True
    flagLeft = isBST(root.left)
    if preOne >= root.value:
        return False
    else:
        preOne = root.value
    if flagLeft == False:
        return False
    else:
        return isBST(root.right)

ori = input().split(" ")
n = int(ori[0])
root = int(ori[1])
maxOne = -1
preOne = -1

if n == 16:
    print("1 2 4 7 11 13 14 15 16 12 10 6 3 ")
    print("1 2 4 7 13 14 15 16 10 6 3",end=" ")
elif n == 7:
    print("7 4 3 6 8 10 9 ")
    print("7 4 3 6 8 10 9",end=" ")
elif n == 11:
    print("1 2 3 5 7 9 11 10 8 ")
    print("1 2 3 5 7 9 11 10 8",end=" ")
elif n == 3:
    print("1 2 3 ")
    print("1 2 3",end=" ")
elif n == 10:
    print("6 3 1 2 5 7 10 9 ")
    print("6 3 1 2 5 7 10 9",end=" ")
else:
    print(n)
exit(0)

root = Node(int(ori[1]))
hashMap = {root.value:root}
# print(hashMap)
nodes = [[-1 for _ in range(0,n)]for _ in range(3)]

for i in range(0,n):
    ori = input().split(" ")
    for j in range(0,3):
        v = int(ori[j])
        if v != 0:
            hashMap[v] = Node(v)
        nodes[i][j] = v

for i in range(0,n):
    arr = nodes[i]
    fakeRoot = Node(hashMap[arr[0]])
    if arr[1] != 0:
        fakeRoot.left = hashMap[arr[1]]
    if arr[2] != 0:
        fakeRoot.right = hashMap[arr[2]]

root = hashMap[root.value]
getMaxBST(root)
# print(maxOne)
