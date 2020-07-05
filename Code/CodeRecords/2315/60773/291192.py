class Node:
    def __init__(self, num, left, right):
        self.val = num
        self.left = left
        self.right = right


def cover(l, n):
    for i in range(len(l)):
        if l[i].val == n:
            return True
    return False


def getDex(l, n):
    for i in range(len(l)):
        if l[i].val == n:
            return l[i]
    return None


def getDepth(root):
    sum = 1
    s1 = 0
    s2 = 0
    if root.left != None:
        s1 = getDepth(root.left)
    if root.right != None:
        s2 = getDepth(root.right)
    sum = sum + max(s1, s2)
    #print(sum)
    return sum


num = int(input())
leaf = []
for i in range(num - 1):
    l = input().split(" ")
    for j in range(2):
        l[j] = int(l[j])
    if cover(leaf, l[0]):
        n1=getDex(leaf, l[0])
    else:
        n1 = Node(l[0], None, None)
        leaf.append(n1)
    #print(n1.val)
    if cover(leaf, l[1]):
        n2 = getDex(leaf, l[1])
    else:
        n2 = Node(l[1], None, None)
        leaf.append(n2)
    #print(n2.val)
    if getDex(leaf, l[0]).left == None:
        getDex(leaf, l[0]).left = getDex(leaf, l[1])
    else:
        getDex(leaf, l[0]).right = getDex(leaf, l[1])
sum = getDepth(leaf[0])
#print(leaf[0].left)
print(sum)




