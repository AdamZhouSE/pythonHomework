class Node:
    def __init__(self, v, l, r):
        self.value = v
        self.left = l
        self.right = r


def makeTree():
    if len(pre) == 0:
        return None
    if pre[0] == " " or pre[0] == "#":
        del (pre[0])
        return None
    else:
        va = pre[0]
        del (pre[0])
        n = Node(va, makeTree(), makeTree())
        return n


def midIndex(root):
    if root is None:
        return ""
    else:
        return midIndex(root.left)+str(root.value)+midIndex(root.right)


pre = list(input())
initial = []
for i in pre:
    initial.append(i)
tree = makeTree()
string = midIndex(tree)
for i in range(len(string)):
    print(string[i], end=" ")
