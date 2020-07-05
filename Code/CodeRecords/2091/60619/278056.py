class Node:
    def __init__(self, v, l, r):
        self.value = v
        self.left = l
        self.right = r


def makeTree(level, appeared):
    if level == 0:
        return Node(-1, makeTree(1, [solve[0][0]]), makeTree(1, [solve[0][1]]))
    else:
        value = appeared[len(appeared) - 1]
        if solve[level][0] in appeared:
            left = None
        else:
            le = [a for a in appeared]
            le.append(solve[level][0])
            left = makeTree(level + 1, le)
        if solve[level][1] in appeared:
            right = None
        else:
            ri = [a for a in appeared]
            ri.append(solve[level][1])
            right = makeTree(level + 1, ri)
        return Node(value, left, right)


def height(root):
    if root is None:
        return 0
    else:
        return 1+max(height(root.left), height(root.right))


li = input().split(" ")
n = int(li[0])
m = int(li[1])
solve = []
for i in range(m):
    solve.append([int(j) for j in input().strip().split(" ")])
tree = makeTree(0, [])
result = height(tree)-1
print(result)