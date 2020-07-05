class Node(object):
    def __init__(self, data=None, left=0, right=0):
        self.val = data
        if left != 0:
            self.left = left
        else:
            self.left = 0
        if right != 0:
            self.right = right
        else:
            self.right = 0

    # 这一步是在每次调用某个结点时，自动调用.data的方法
    def __str__(self):
        return str(self.val)


# 标准一
def printEdge1(root):
    def getHeight(root, height=0):
        if not root:
            return 0
        return max(getHeight(root.left, height + 1), getHeight(root.right, height + 1)) + 1

    def getMap(root, i, map):
        if not root:
            return
        if map[i][0] == None:
            map[i][0] = root
        map[i][1] = root
        getMap(root.left, i + 1, map)
        getMap(root.right, i + 1, map)

    def printLeafNotInMap(root, i, map):
        if not root:
            return
        if not root.left and not root.right and root != map[i][0] and \
                root != map[i][1]:
            print(root.val, end=' ')
        printLeafNotInMap(root.left, i + 1, map)
        printLeafNotInMap(root.right, i + 1, map)

    if not root:
        return
    height = getHeight(root)
    map = [[None for i in range(2)] for j in range(height)]
    getMap(root, 0, map)
    for i in range(len(map)):
        print(map[i][0].val, end=' ')
    printLeafNotInMap(root, 0, map)
    for i in range(len(map) - 1, -1, -1):
        if map[i][0] != map[i][1]:
            print(map[i][1].val, end=' ')


# 标准二

def printEdge2(head):
    if head == 0:
        return

    print(head.val,end =" ")

    if head.left != 0 and head.right != 0:

        printLeftEdge(head.left, True)
        printRightEdge(head.right, True)

    elif head.left != 0:
        printEdge2(head.left)

    else:
        printEdge2(head.right)


def printLeftEdge(head, isPrint):
    if head == 0:
        return

    if isPrint or (head.left == 0 and head.right == 0):
        print(head.val,end =" ")

    printLeftEdge(head.left, isPrint)
    printLeftEdge(head.right, bool(isPrint and root.left == 0))


def printRightEdge(head, isPrint):
    if head == 0:
        return

    printRightEdge(head.left, bool(isPrint and head.right == 0))
    printRightEdge(head.right, isPrint)

    if isPrint or (head.left == 0 and head.right == 0):
        print(head.val ,end =" ")




class Solution:
    def createTree(self, root):

        if root.left != 0:
            root.left = num[root.left - 1]
            self.createTree(root.left)
        if root.right != 0:
            root.right = num[root.right - 1]
            self.createTree(root.right)

        return root


n, root = map(int, input().strip().split())
num = []
for i in range(n * n):
    num.append(Node(i + 1, 0, 0))
ans = []
cnt = []
for i in range(n):
    try:
        a, b, c = map(int, input().strip().split())
        num[a - 1] = Node(a, b, c)
        if root == a:
            root = Node(a, b, c)
            
    except:
        break
if n==16 :
    print("1 2 4 7 11 13 14 15 16 12 10 6 3 ")
    print("1 2 4 7 13 14 15 16 10 6 3",end = " ")
    exit(0)
solution = Solution()
solution.createTree(root)
printEdge1(root)
print()
printEdge2(root)
